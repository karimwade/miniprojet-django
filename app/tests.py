from django.test import TestCase,Client
from .models import Student
from django.urls import reverse
# Create test model Student
class StudentModelTest(TestCase):
    def setUp(self):
        #Creation d'un eleve pour les tests
        self.student=Student.objects.create(name="papa test",mail="papa@gmail.com",gender="Male")
        
        #Ceci est une methode de faire un test en verifiant le nombre d'enregistrement avant et apres en faisant la comparaison
#----------------------------------------------------------------------------#
    # def test_student_creation(self):
    #     #Creation et verification de l'insertion
    #     #ceci est une methode de faire un test
    #     nbre_befor_save= Student.objects.count()
    #     new_student=Student()
    #     new_student.name= 'papa test'
    #     new_student.mail= 'test@gmail.com'
    #     new_student.gender = 'Male'
    #     new_student.save()
    #     nbre_after_save=Student.objects.count()
    #     self.assertTrue(nbre_after_save == nbre_befor_save +1)
#----------------------------------------------------------------------------#
    def test_student_creation(self):
        # Données pour la création d'un nouvel étudiant
        name = 'Maniouk Badiane'
        mail = 'mbadiane@example.com'
        gender = 'Male'

        # URL de la vue de création (insert)
        url = reverse('insert')

        # Effectuer la requête POST pour créer un nouvel étudiant
        response = self.client.post(url, {'name': name, 'mail': mail, 'gender': gender})

        # Vérifier que la requête a réussi (code de statut HTTP 200 ou 302)
        self.assertTrue(response.status_code in [200, 302])

        # Vérifier que l'étudiant a été créé dans la base de données
        self.assertTrue(Student.objects.filter(name=name, mail=mail, gender=gender).exists())

    # def test_read_student(self):
    #     # URL de la vue de détail (read)
    #     #url= reverse('index')
    #     #response = self.client.get(url)
    #     url = reverse('insert', kwargs={'pk': self.student.pk})

    #     # Effectuer la requête GET pour obtenir les détails de l'étudiant
    #     response = self.client.get(url)

    #     # Vérifier que la requête a réussi (code de statut HTTP 200)
    #     self.assertEqual(response.status_code, 200)

    #     # Vérifier que les données de l'étudiant sont correctes
    #     self.assertEqual(response.context['student'].name, self.student.name)
    #     self.assertEqual(response.context['student'].mail, self.student.mail)
    #     self.assertEqual(response.context['student'].gender, self.student.gender)

    def test_update_student(self):
        # -----------------1er methode--------------------------#
        # # Nouvelles données pour la mise à jour de l'étudiant
        # new_name = 'Updated Name'
        # new_mail = 'updatedmail@example.com'
        # new_gender = 'Other'

        # self.student.name = new_name
        # self.student.mail = new_mail
        # self.student.gender =new_gender
        # self.student.save()

        # #Actualiser l'objet depuis la base données 
        # self.student.refresh_from_db()
        # # Vérifier que les données ont été correctement mises à jour
        # self.assertEqual(self.student.name, new_name)
        # self.assertEqual(self.student.mail, new_mail)
        # self.assertEqual(self.student.gender, new_gender)
        #-------------2e methode---------------------------#
        new_name = 'Deuxieme test'
        new_mail = 'deuxieme@exemple.com'
        new_gender = 'Female'

        # Mise à jour de l'objet MyModel en utilisant la méthode 'update'
        Student.objects.filter(pk=self.student.pk).update(name=new_name, mail=new_mail, gender=new_gender)

        # Récupérer l'objet depuis la base de données pour vérifier les modifications
        updated_mymodel = Student.objects.get(pk=self.student.pk)

        # Vérifier que les données ont été correctement mises à jour
        self.assertEqual(updated_mymodel.name, new_name)
        self.assertEqual(updated_mymodel.mail, new_mail)
        self.assertEqual(updated_mymodel.gender, new_gender)

    #test delete
    def test_delete_mymodel(self):
        # Suppression de l'objet MyModel
        self.student.delete()

        # Vérifier que l'objet a été supprimé de la base de données
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
    
        
#Test Views app
class view_app_test(TestCase):
    def set_up(self):
        self.client = Client()

    def test_index(self):
        url= reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
