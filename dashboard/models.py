from django.db import models
import json

class LocalizacaoGeografica(models.Model):
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=40)
    municipio = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    quadra = models.CharField(max_length=10)
    lote = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"LocalizaçãoGeografica: {self.pais}, {self.estado}, {self.municipio}, {self.bairro}"

class OficioNotarial(models.Model):
    notarialCountry = models.CharField(max_length=100)
    notarialStates = models.CharField(max_length=100)
    notarialMunicipality = models.CharField(max_length=100)
    notarialNeighborhood = models.CharField(max_length=100)
    notarialStreet = models.CharField(max_length=100)
    notarialBlock = models.CharField(max_length=100)
    notarialLot = models.CharField(max_length=100)
    notarialRegistration = models.CharField(max_length=100)

    # Se necessário, adicione mais campos ou métodos aqui

    def __str__(self):
        return f"Ofício Notarial - {self.notarialMunicipality}, {self.notarialCountry}"

class Prefeitura(models.Model):
    addressCountry = models.CharField(max_length=100)
    addressStates = models.CharField(max_length=40)
    municipality = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    block = models.CharField(max_length=10)
    lot = models.CharField(max_length=10)
    iptuRegistration = models.CharField(max_length=100)

    def __str__(self):
        return f"Prefeitura: {self.addressCountry}, {self.addressStates}, {self.municipality}, {self.neighborhood}"

class Topografo(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    registro = models.CharField(max_length=20)  # Número de registro profissional

    class Meta:
        verbose_name = 'Topógrafo'
        verbose_name_plural = 'Topógrafos'

class Engenheiro(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    registro = models.CharField(max_length=20)  # Número de registro profissional

    class Meta:
        verbose_name = 'Engenheiro'
        verbose_name_plural = 'Engenheiros'

class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    registro = models.CharField(max_length=20)  # Número de registro profissional

    class Meta:
        verbose_name = 'Advogado'
        verbose_name_plural = 'Advogados'

class Imovel(models.Model):
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    currency_venda = models.CharField(max_length=3)
    preco_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    currency_aluguel = models.CharField(max_length=3)
    categoria = models.CharField(max_length=100)
    comodos = models.CharField(max_length=200)

    def __str__(self):
        return f'Imóvel {self.id}'

class PlanoArquitetonico(models.Model):
    metros_quadrados = models.DecimalField(max_digits=10, decimal_places=2)
    art_numero = models.CharField(max_length=100)

    def __str__(self):
        return f"Plano Arquitetônico - ART: {self.art_numero}"

class Topografia(models.Model):
    zona_utm = models.IntegerField()
    meridiano_central = models.IntegerField()
    latitude_utm = models.FloatField()
    longitude_utm = models.FloatField()
    sistema_geodesico = models.CharField(max_length=100)

    def __str__(self):
        return f"Topografia {self.id}"

class PlanoDeZoneamento(models.Model):
    ZONAMENTO_CHOICES = [
        ('ZR1', 'Zona Residencial (ZR1)'),
        ('ZR2', 'Zona Residencial (ZR2)'),
        ('ZR3', 'Zona Residencial (ZR3)'),
        ('ZRE', 'Zona Residencial Especial (ZRE)'),
        ('ZC1', 'Zona Comercial (ZC1)'),
        ('ZC2', 'Zona Comercial (ZC2)'),
        ('ZC3', 'Zona Comercial (ZC3)'),
        ('ZCE', 'Zona Comercial Especial (ZCE)'),
        ('ZI1', 'Zona Industrial (ZI1)'),
        ('ZI2', 'Zona Industrial (ZI2)'),
        ('ZI3', 'Zona Industrial (ZI3)'),
        ('ZIE', 'Zona Industrial Especial (ZIE)'),
        ('ZPA', 'Zona de Preservação Ambiental (ZPA)'),
        ('ZPR', 'Zona de Proteção Ambiental (ZPR)'),
        ('ZRA', 'Zona de Recuperação Ambiental (ZRA)'),
        ('ZR', 'Zona Rural (ZR)'),
        ('ZA', 'Zona Agrícola (ZA)'),
    ]

    zoneamento = models.CharField(max_length=20, choices=ZONAMENTO_CHOICES)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Zoneamento: {self.get_zoneamento_display()}"

class EscrituraImobiliaria(models.Model):
    # Campos da escritura imobiliária
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    # Adicione mais campos conforme necessário

    # Campo para a localização geográfica
    localizacao_geografica = models.OneToOneField('LocalizacaoGeografica', on_delete=models.CASCADE, related_name='escritura_imobiliaria')

    # Método para carregar os dados do banco de dados
    def carregar_dados(self):
        # Lógica para carregar os dados do banco de dados
        # Por exemplo:
        self.campo1 = 'valor1'
        self.campo2 = 123
        # Carregar também os dados da localização geográfica

    # Método para preencher os formulários
    def preencher_formularios(self):
        # Lógica para preencher os formulários com os dados carregados
        # Por exemplo:
        if self.localizacao_geografica:
            formulario_localizacao = {
                'pais': self.localizacao_geografica.pais,
                'estado': self.localizacao_geografica.estado,
                # Preencher os outros campos do formulário de localização geográfica
            }
            return json.dumps(formulario_localizacao)
        else:
            return ''

    # Método para verificar o progresso de preenchimento
    def verificar_progresso(self):
        # Lógica para verificar se todos os formulários foram preenchidos
        # Por exemplo:
        if self.campo1 and self.campo2 and self.localizacao_geografica:
            return True
        return False

    # Método para converter em JSON
    def converter_em_json(self):
        # Lógica para converter os dados preenchidos em JSON
        # Por exemplo:
        dados = {
            'campo1': self.campo1,
            'campo2': self.campo2,
            # Adicione outros campos conforme necessário
        }
        return json.dumps(dados)