from django.db import models

# Create a model for quizzes
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create a model for quiz questions
class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1)  # Default to the first quiz in the database.
    question_text = models.TextField(default="Enter your question here")
    option1 = models.CharField(max_length=200, default="Option 1")
    option2 = models.CharField(max_length=200, default="Option 2")
    option3 = models.CharField(max_length=200, default="Option 3")
    option4 = models.CharField(max_length=200, default="Option 4")
    correct_option = models.CharField(max_length=1, choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')], default='1')

    def __str__(self):
        return self.question_text
