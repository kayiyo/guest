from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User

# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name='3 event', status=True,
                             limit=2000, address='Beijing', start_time='2018-8-2')
        Guest.objects.create(id=1, event_id=1, real_name='Alex',
                             phone='13701231234', email='Alex@gg.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='3 event')
        self.assertEqual(result.address, 'Beijing')
        self.assertTrue(result.status)

    def test_guest_model(self):
        result = Guest.objects.get(phone='13701231234')
        self.assertEqual(result.real_name, 'Alex')
        self.assertFalse(result.sign)


class IndexPageTest(TestCase):
    ''' 测试index登录首页'''

    def test_index_page_randers_index_template(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    '''测试登录动作'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_admin(self):
        '''测试添加用户'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@mail.com')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''

        test_data = {'username':'', 'password':''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''

        test_data = {'username':'abc', 'password':'123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        '''登录成功'''

        test_data = {'username':'admin', 'password':'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
    '''发布会管理'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name='xm5', limit=2000, address='beijing',
                             status=1,start_time='2018-8-2 12:30:00')
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_event_manage_success(self):
        '''测试发布会xm5'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xm5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_event_manage_search_success(self):
        '''测试发布会搜索'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name': 'xm5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xm5', response.content)
        self.assertIn(b'beijing', response.content)
