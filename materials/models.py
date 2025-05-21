from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/previews/", blank=True, null=True, verbose_name="Картинка"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        """
        Строковое представление курса.
        Returns:
            str: Название курса.
        """
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    preview = models.ImageField(
        upload_to="materials/previews/", blank=True, null=True, verbose_name="Картинка"
    )
    video_link = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Ссылка на видео"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Выберите курс"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        """
        Строковое представление урока.
        Returns:
            str: Название урока.
        """
        return self.name
