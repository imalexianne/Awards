from django.test import TestCase
from .models import Project,Profile

# Create your tests here.
class ImageTestClass(TestCase):

    # # Set up method
    # def setUp(self):
    #     self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')


    # # Testing  instance
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.james,Editor))
    
    # Testing Save Method
    def test_save_method(self):
        self.baby1.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.baby1.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # def test_display_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

    def test_update_method(self):
        self.baby1.save_image()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # def setUp(self):
    #     # Creating a new editor and saving it
    #     self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    #     self.james.save_editor()

    #     # Creating a new tag and saving it
    #     self.new_tag = tags(name = 'testing')
    #     self.new_tag.save()

    #     self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
    #     self.new_article.save()

    #     self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        # location.objects.all().delete()


    def test_get_project_by_id(id):
        project = Project.project()
        self.assertTrue(len(project)>0)


# Create your tests here.
