from django.test import TestCase
from.models import Teacher
import datetime
from.forms import TeacherForm
from django.urls import reverse
from django.test import Client
client=Client()


class CreateTeacherTestCase(TestCase):
	def setUp(self):
		self.data={
		"first_name":"chesang",
		"last_name":"Felister",
		"regestration_number":"6677865",
		'place_of_resident':"Kilimani",
		"phone_number":"076533323",
		'email':"chesangfelister@gmail.com",
		'Id_number':"987768787",
		"date_joined":datetime.date.today(),
		"profession":"Developer"
	
		}
		self.bad_data={
		"first_name":"chesang",
		"last_name":"Felister",
		"regestration_number":"6677865",
		"place_of_resident":"Kilimani",
		"phone_number":"076533323",
		"email":"chesangfelister@gmail.com",
		"Id_number":"987768787",
		"date_joined":"datetime.date.today()",
		"profession":"Developer"
		}

	
	def test_teacher_form_always_valid_data(self):
		form=TeacherForm(self.data)
		self.assertTrue(form.is_valid())

		
	def test_bad_teacher_form_reject_invalid_data(self):
		form=TeacherForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_teacher_view(self):
		url=reverse("add_teacher")
		request=client.post(url,self.data)
		self.assertEqual(request.status_code,200)
	def test_add_teacher_view_bad_data(self):
		url=reverse("add_teacher")
		request=client.post(url,self.bad_data)
		self.assertEqual(request.status_code,400)



# Create your tests here.
