import getpass
import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from sesame import utils
# from .utils.api_utils import get_yml_file
# from .utils.db_utils import DBUtils
from .srializers import CustomUserSerializer

LOGGER = logging.getLogger(__name__)


class UserAPI(APIView):
    """
    apis performs as per given request
    """

    def __init__(self, **kwargs):
        super(UserAPI, self).__init__(**kwargs)
        self.User = get_user_model()
        # self.db_utils_obj = DBUtils()

    def get(self, request):
        """
        check user exist or not api
        """

        LOGGER.debug("Inside User Get api method")
        LOGGER.debug("request data are: %s", request.query_params)
        permission_class = (IsAuthenticated)
        serializer_class = CustomUserSerializer.get_value()


        # return_dict = dict()
        # if 'email_id' in request.query_params and request.query_params['email_id']:
        #     if self.User.objects.filter(username__iexact=request.query_params['email_id']).exists():
        #         user_id = self.User.objects.get(username__iexact=request.query_params['email_id']).id
        #         return_dict['user_id'] = user_id
        #     else:
        #         LOGGER.debug("User ID is Empty")
        #         return_dict['message'] = "User is not exists"
        #     return_status = status.HTTP_200_OK
        # else:
        #     return_status = status.HTTP_400_BAD_REQUEST
        #     return_dict['status_code'] = return_status
        #     return_dict['message'] = 'Invalid request. A required parameter was not provided.'
        # return Response(data=return_dict, status=return_status)


# def post(self, request):
#         """
#         Create records for user as given request
#         """
#
#         LOGGER.debug("Inside User Post api method")
#         LOGGER.debug("Request Data are: %s", request.data)
#         return_dict = dict()
#
#         config_file = get_square_deal_yml_file()
#
#         if 'email_id' in request.data and request.data['email_id']:
#             password = self.User.objects.make_random_password()
#
#             # check email exist or not
#             if self.User.objects.filter(username__iexact=request.data['email_id']).exists():
#                 LOGGER.debug("user already exists.")
#                 user = self.User.objects.get(username__iexact=request.data['email_id'])
#                 user.set_password(password)
#                 # Update user first and last names
#                 fname = request.data.get('first_name', None)
#                 lname = request.data.get('last_name', None)
#                 if fname and lname:
#                     user.first_name = fname
#                     user.last_name = lname
#
#                 user.save()
#                 LOGGER.debug("Reset password.")
#
#                 # update or create user password expiry table
#                 if user.is_superuser is False or user.is_staff is False:
#                     self.update_or_create_user_password_expiry(
#                         user_id=user.id,
#                         user_password_expiry_time=config_file['user_password_expiry_time'])
#                 else:
#                     LOGGER.debug("Given user is super user or staff")
#
#                 if 'tenant_id' in request.data and request.data['tenant_id']:
#                     # check user id and tenant id exist or not
#                     tenant_id = request.data['tenant_id']
#                     LOGGER.debug("Tenant ID: %s", tenant_id)
#
#                     if CustomUser.objects.filter(tenant_id=tenant_id,
#                                                  user_id=user.id).exists():
#                         LOGGER.debug("user and tenant already exist")
#                     else:
#                         CustomUser.objects.create(**{
#                             "tenant_id": tenant_id,
#                             "user_id": user.id,
#                             "create_user": getpass.getuser(),
#                             "create_program": self.get_view_name(),
#                             "modify_user": getpass.getuser(),
#                             "modify_program": self.get_view_name()
#                         })
#                     LOGGER.debug("User : %s", user)
#
#                 else:
#                     LOGGER.debug("given user request comes from square deal b2c")
#
#                 return_status = status.HTTP_200_OK
#                 return_dict['message'] = "User already exists"
#                 return_dict['user_id'] = user.id
#                 return_dict['temp_passcode'] = password
#             else:
#                 LOGGER.debug("New user..now creating...")
#
#                 try:
#                     user_dict = {
#                         "username": request.data['email_id'],
#                         "email": request.data['email_id'],
#                     }
#                     if 'first_name' in request.data:
#                         user_dict["first_name"] = request.data['first_name']
#
#                     if 'last_name' in request.data:
#                         user_dict["last_name"] = request.data['last_name']
#
#                     if 'middle_initial' in request.data:
#                         user_dict["middle_initial"] = request.data["middle_initial"]
#
#                     if 'phone_number' in request.data:
#                         user_dict["phone_number"] = request.data['phone_number']
#
#                     if 'company_name' in request.data:
#                         user_dict["company_name"] = request.data['company_name']
#
#                     if 'profile_pic_url' in request.data:
#                         user_dict["image_url"] = request.data['profile_pic_url']
#
#                     user = self.User.objects.create(**user_dict)
#                     user.set_password(password)
#                     user.save()
#                     LOGGER.debug("User: %s", user)
#
#                     # update or create user password expiry table
#                     if user.is_superuser is False or user.is_staff is False:
#                         self.update_or_create_user_password_expiry(
#                             user_id=user.id,
#                             user_password_expiry_time=config_file['user_password_expiry_time']
#                         )
#                     else:
#                         LOGGER.debug("Given user is super user or staff")
#
#                     if 'tenant_id' in request.data and request.data['tenant_id']:
#                         tenant_id = request.data['tenant_id']
#                         LOGGER.debug("Tenant ID: %s", tenant_id)
#
#                         CustomUser.objects.create(**{
#                             "user_id": user.id,
#                             "tenant_id": tenant_id,
#                             "create_user": getpass.getuser(),
#                             "create_program": self.get_view_name(),
#                             "modify_user": getpass.getuser(),
#                             "modify_program": self.get_view_name()
#                         })
#
#                     else:
#                         LOGGER.debug("given user request comes from square deal b2c")
#                     return_dict['user_id'] = user.id
#                     return_dict['temp_passcode'] = password
#
#                     return_status = status.HTTP_201_CREATED
#
#                 except KeyError as ke_err:
#                     LOGGER.debug("Key error: %s", ke_err)
#                     return_status = status.HTTP_400_BAD_REQUEST
#                     return_dict['message'] = 'key error' + str(ke_err)
#                     return Response(data=return_dict, status=return_status)
#                 except Exception as ex_err:
#                     return_status = status.HTTP_400_BAD_REQUEST
#                     return_dict['message'] = 'Exception Error' + str(ex_err)
#                     return Response(data=return_dict, status=return_status)
#
#             if 'email_password' in request.data and request.data['email_password']:
#
#                 # create magic token
#                 login_token = utils.get_query_string(user)
#                 LOGGER.debug("login token: %s", login_token)
#                 # combine login host and sesame(magic token)
#                 # login_link = config_file['login_host'] + '/magicAuth' + login_token + '&email={0}'.format(
#                 #     request.data['email_id']) + '&temp_code={0}'.format(
#                 #     password) + '&redirectURL={0}'.format(config_file['redirect_url'])
#                 # LOGGER.debug("Login link: %s", login_link)
#
#                 email_password = {
#                     "password": password,
#                 }
#                 if 'first_name' in request.data and request.data['first_name']:
#                     email_password.update({'first_name': request.data['first_name']})
#
#                 if 'last_name' in request.data and request.data['last_name']:
#                     email_password.update({'last_name': request.data['last_name']})
#
#                 LOGGER.debug("sending email.")
#                 post_dict = {
#                     "post_set": email_password,
#                     "template_name": 'email_password.html',
#                     "subject": 'Welcome to Square Deal',
#                     "recipient": request.data['email_id']
#                 }
#                 send_email.delay(post_set=post_dict)
#                 LOGGER.debug("async task created.")
#             else:
#                 LOGGER.debug("user already exists, not send password to user")
#         else:
#             return_status = status.HTTP_400_BAD_REQUEST
#             return_dict['message'] = 'Invalid request. A required parameter was not provided.'
#             return_dict['status_code'] = return_status
#
#         return Response(data=return_dict, status=return_status)
