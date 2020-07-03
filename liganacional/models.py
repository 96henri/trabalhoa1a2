from django.db import models

from django.db import models


class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=100, blank=False)
    academiaProfessor = models.ForeignKey("Academia", on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeProfessor

    class Meta:
        verbose_name_plural = "Professores"


class Academia(models.Model):
    nomeAcademia = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nomeAcademia

    class Meta:
        verbose_name_plural = "Academias"


class Federacao(models.Model):
    nomeFederacao = models.CharField(max_length=100, primary_key=True, blank=False)
    cidadeFederacao = models.CharField(max_length=100, blank=False)
    professores = models.OneToOneField(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeFederacao

    class Meta:
        verbose_name_plural = "Federações"


class Lutas(models.Model):
    ESTADO_CHOICES = (
        ("Acre", "Acre"),
        ("Alagoas", "Alagoas"),
        ("Amapá", "Amapá"),
        ("Amazonas", "Amazonas"),
        ("Bahia", "Bahia"),
        ("Ceará", "Ceará"),
        ("Distrito Federal", "Distrito Federal"),
        ("Espírito Santo", "Espírito Santo"),
        ("Goiás", "Goiás"),
        ("Maranhão", "Maranhão"),
        ("Mato Grosso", "Mato Grosso"),
        ("Mato Grosso do Sul", "Mato Grosso do Sul"),
        ("Minas Gerais", "Minas Gerais"),
        ("Pará", "Pará"),
        ("Paraíba", "Paraíba"),
        ("Paraná", "Paraná"),
        ("Pernambuco", "Pernambuco"),
        ("Piauí", "Piauí"),
        ("Rio de Janeiro", "Rio de Janeiro"),
        ("Rio Grande do Norte", "Rio Grande do Norte"),
        ("Rio Grande do Sul", "Rio Grande do Sul"),
        ("Rondônia", "Rondônia"),
        ("Santa Catarina", "Santa Catarina"),
        ("São Paulo", "São Paulo"),
        ("Sergipe", "Sergipe"),
        ("Tocantins", "Tocantins")

    )
    nomeEvento = models.CharField(max_length=100, blank=False, null=False, default="")
    estadoLuta = models.CharField(max_length=100, choices=ESTADO_CHOICES, blank=False, null=False)
    federacaoCamp = models.ManyToManyField(Federacao)
    dataCamp = models.CharField(max_length=8, blank=False, null=False, default="dd/mm/aaaa")



    def __str__(self):
        return self.estadoLuta

    class Meta:
        verbose_name_plural = "Datas de Campeonatos"


class Aluno(models.Model):
    CATEGORIA_CHOICES = (
        ("Amador 50/54kg", "Amador 50/54kg"),
        ("Amador 55/59kg", "Amador 55/59kg"),
        ("Amador 60/64kg", "Amador 60/64kg"),
        ("Amador 65/69kg", "Amador 65/69kg"),
        ("Amador 70/74kg", "Amador 70/74kg"),
        ("Amador 75/79kg", "Amador 75/79kg"),
        ("Amador PERSONALIZADA", "Amador Personalizada"),
        ("Semi Pro 50/54kg", "Semi Pro 50/54kg"),
        ("Semi Pro 55/59kg", "Semi Pro 55/59kg"),
        ("Semi Pro 60/64kg", "Semi Pro 60/64kg"),
        ("Semi Pro 65/69kg", "Semi Pro 65/69kg"),
        ("Semi Pro 70/74kg", "Semi Pro 70/74kg"),
        ("Semi Pro 75/79kg", "Semi Pro 75/79kg"),
        ("Semi Pro PERSONALIZADA", "Semi Pro Personalizada"),
        ("Profissional 50/54kg", "Profissional 50/54kg"),
        ("Profissional 55/59kg", "Profissional 55/59kg"),
        ("Profissional 60/64kg", "Profissional 60/64kg"),
        ("Profissional 65/69kg", "Profissional 65/69kg"),
        ("Profissional 70/74kg", "Profissional 70/74kg"),
        ("Profissional 75/79kg", "Profissional 75/79kg"),
        ("Profissional PERSONALIZADA", "Profissional Personalizada"),
    )
    nomeAluno = models.CharField(max_length=100, blank=False, null=False, default="")
    rua = models.CharField(max_length=100, blank=False, null=False, default="")
    numero = models.CharField(max_length=6, blank=False, null=False, default="0")
    bairro = models.CharField(max_length=50, blank=False, null=False, default="")
    categorias = models.CharField(max_length=100, choices=CATEGORIA_CHOICES, blank=False, null=False, default="")
    academiaTreino = models.ManyToManyField(Academia)

    def __str__(self):
        return self.nomeAluno

    class Meta:
        verbose_name_plural = "Alunos"

