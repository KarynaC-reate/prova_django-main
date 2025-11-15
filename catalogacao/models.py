from django.db import models

# --- Entidade Tipo (Meta-Categoria) ---
class Tipo(models.Model):
    """
    Representa uma categoria ampla para Gêneros (ex: Literário, Jornalístico, Acadêmico).
    """
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Tipo")

    class Meta:
        verbose_name = "Tipo de Gênero"
        verbose_name_plural = "Tipos de Gêneros"

    def __str__(self):
        return self.nome


# --- Entidade Genero (A Categoria Principal) ---
class Genero(models.Model):
    """
    Representa o Gênero Textual específico (ex: Notícia, Poema, Receita).
    Relaciona-se com Tipo (1:N).
    """
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Gênero")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Gênero")

    # Relação 1:N com Tipo
    tipo = models.ForeignKey(
        Tipo,
        on_delete=models.SET_NULL,  # Mantém o Gênero se o Tipo for deletado (seta para NULL)
        null=True,
        blank=True,
        verbose_name="Tipo Associado"
    )

    class Meta:
        verbose_name = "Gênero Textual"
        verbose_name_plural = "Gêneros Textuais"

    def __str__(self):
        return f"{self.nome} ({self.tipo.nome if self.tipo else 'Sem Tipo'})"


# --- Entidade Documento (O Texto em Si) ---
class Documento(models.Model):
    """
    Representa o documento (texto) a ser catalogado.
    Relaciona-se com Genero (1:N).
    """
    titulo = models.CharField(max_length=255, verbose_name="Título do Documento")

    # O conteúdo do texto (o documento em si)
    conteudo = models.TextField(verbose_name="Conteúdo Completo do Texto")

    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    # Relação 1:N com Genero
    genero = models.ForeignKey(
        Genero,
        on_delete=models.PROTECT,  # Impede a exclusão do Gênero se houver documentos associados
        verbose_name="Gênero Textual"
    )

    class Meta:
        verbose_name = "Documento Catalogado"
        verbose_name_plural = "Documentos Catalogados"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"[{self.genero.nome}] {self.titulo}"