from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Supervisor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    qualif = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='media/supervisors_images/')


    def __str__(self):
        return self.user.first_name



class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    team_name = models.CharField(max_length=200, null=True, blank=True)
    team_leader_name = models.CharField(max_length=200, null=True, blank=True)
    team_leader_roll = models.CharField(max_length=200, null=True, blank=True)
    member2_name = models.CharField(max_length=200, null=True, blank=True)
    member2_roll = models.CharField(max_length=200, null=True, blank=True)
    member3_name = models.CharField(max_length=200, null=True, blank=True)
    member3_roll = models.CharField(max_length=200, null=True, blank=True)
    dept = models.CharField(max_length=30, null=True, blank=True)
    member1_pic = models.ImageField(upload_to='media/students/', null=True, blank=True)
    member2_pic = models.ImageField(upload_to='media/students/', null=True, blank=True)
    member3_pic = models.ImageField(upload_to='media/students/', null=True, blank=True)
    featured_image = models.ImageField(upload_to='media/projects_img/', null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, null=True, blank=True)
    rating_review = models.ManyToManyField('Project_Reviews', default=None, blank=True)

    def __str__(self):
        return f"({self.team_leader_name}-{self.dept})"


class Reviewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    qualif = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='media/reviewers_images/', null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name + "( " + self.qualif + ")"


class Project_Reviews(models.Model):
    review_text = models.TextField(null=True, blank=True)
    rating1 = models.IntegerField(null=True, blank=True)
    rating2 = models.IntegerField(null=True, blank=True)
    rating3 = models.IntegerField(null=True, blank=True)
    rating4 = models.IntegerField(null=True, blank=True)
    total_rating = models.IntegerField(null=True, blank=True)
    project_team = models.ForeignKey(Project, null=True, on_delete=models.CASCADE,  blank=True)
    reviewer = models.ForeignKey(Reviewer, null=True, on_delete=models.CASCADE,  blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_team + " by " + self.reviewer



