from logging import raiseExceptions
from django.contrib.auth import tokens
from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode


class RegisterSerializers(serializers.ModelSerializer):
  password=serializers.CharField(max_length=68, min_length=6, write_only=True)

  class Meta:
    model=User
    fields=['email','username','password']

  def validate(self, attrs):
    email=attrs.get('email','')
    username=attrs.get('username','')

    if not username.isalnum():
      raise serializers.ValidationError('Username should only contain char alphanumerics')
    

    return attrs
  
  def create(self, validated_data):
      return User.objects.create_user(**validated_data)
    
class EmailVerificationSerializer(serializers.ModelSerializer):
  token=serializers.CharField(max_length=555)
  class Meta:
    model=User
    fields=['token']

class LoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=255, min_length=3 )
  password = serializers.CharField(max_length=68, min_length=2, write_only=True)
  email = serializers.EmailField(max_length=255, min_length=3, read_only=True)
  tokens = serializers.CharField(max_length=255, min_length=3, read_only=True)

  class Meta:
    model = User
    fields = ['email','password','username','tokens']

  def validate(self,attrs):
    # email = attrs.get('email', '')
    username = attrs.get('username', '')
    password = attrs.get('password','')
    user = auth.authenticate(username=username,password=password)
    # import pdb
    # pdb.set_trace()
    if not user:
      raise AuthenticationFailed({'Invalid credentials, Try again'})

    if not user.is_active:
      raise AuthenticationFailed({'Account disabled, please contact admin'})

    if not user.is_verified:
      raise AuthenticationFailed({'Email is not verified'})
    
    return {
      'username': user.username,
      'email': user.email,
      'tokens': user.tokens()
    }    

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
  email=serializers.EmailField(min_length=2)
  class Meta:
    fields=['email']


class SetNewPasswordSerializer(serializers.Serializer):
  password = serializers.CharField(min_length=6, max_length=68,write_only=True)
  token = serializers.CharField(min_length=1,write_only=True)
  uidb64 = serializers.CharField(min_length=1,write_only=True)
  class Meta:
    fields=['password','uidb64','token']
  def validate(self, attrs):
    try:
      password = attrs.get('password')
      token = attrs.get('token')
      uidb64 = attrs.get('uidb64')
      id = force_str(urlsafe_base64_decode(uidb64))
      user = User.objects.get(id=id)

      if not PasswordResetTokenGenerator().check_token(user, token):
        raise AuthenticationFailed('The reset link is invalid',401)

      user.set_password(password)
      user.save()

      return (user)
    except Exception as e:
        raise AuthenticationFailed('The reset link is invalid',401)

    return super().validate(attrs)



    