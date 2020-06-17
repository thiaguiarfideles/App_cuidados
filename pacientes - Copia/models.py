#coding: utf-8

from django.db import models
from django.utils import timezone
from usuarios.models import User
from core.helpers import validate_file_extension



STATUS_CONVENIOS = (
('ALLIANZ', 'ALLIANZ'),
('FIOSAÚDE', 'FIOSAÚDE'),
('PAME', 'PAME'),
('UNAFISCO SAÚDE', 'UNAFISCO SAÚDE'),
('DIX', 'DIX'),
('GOLDEN CROSS', 'GOLDEN CROSS'),
('BRADESCO', 'BRADESCO'),
('BANCO CENTRAL DO BRASIL', 'BANCO CENTRAL DO BRASIL'),
('PARTICULAR', 'PARTICULAR'),
('CASSI', 'CASSI'),
('IPALERJ', 'IPALERJ'),
('AMIL', 'AMIL'),
('VALE S. A.', 'VALE S. A.'),
('BNDES/FAPES', 'BNDES/FAPES'),
('REAL GRANDEZA', 'REAL GRANDEZA'),
('PETROBRAS PETRÓLEO', 'PETROBRAS PETRÓLEO'),
('MEDISERVICE', 'MEDISERVICE'),
('SUL AMERICA', 'SUL AMERICA'),
('EMBRATEL', 'EMBRATEL'),
('TELOS', 'TELOS'),
('EMBRATELPRIMESYS', 'EMBRATELPRIMESYS'),
('PETROBRAS DISTRIBUIDORA', 'PETROBRAS DISTRIBUIDORA'),
('CARE PLUS', 'CARE PLUS'),
('BNDES/FAPES', 'BNDES/FAPES'),
('PARTICULAR', 'PARTICULAR'),
('UNAFISCO', 'UNAFISCO'),
('GOLDEN CROSS', 'GOLDEN CROSS'),
('SUL AMÉRICA', 'SUL AMÉRICA'),
('TELOS', 'TELOS'),
('ASSEFAZ', 'ASSEFAZ'),
('CLARO (EMBRATEL)', 'CLARO (EMBRATEL)'),
('ALLIANZ', 'ALLIANZ'),
('REAL GRANDEZA', 'REAL GRANDEZA'),
('CABERJ', 'CABERJ'),
('ASSEFAZ', 'ASSEFAZ'),
('INTERMÉDICA', 'INTERMÉDICA'),
('BANCO CENTRAL', 'BANCO CENTRAL'),
('INTERMÉDICA', 'INTERMÉDICA'),
('PETROBRAS PETROLEO', 'PETROBRAS PETROLEO'),
('GAMA SAÚDE', 'GAMA SAÚDE'),
('LIFE EMPRESARIAL', 'LIFE EMPRESARIAL'),
('UNIMED RIO', 'UNIMED RIO'),
('UNIMED COSTA VERDE', 'UNIMED COSTA VERDE'),
('CAMPERJ', 'CAMPERJ'),
('CAMARJ', 'CAMARJ'),
('CAMARJ', 'CAMARJ'),
('CENTRAL NACIONAL UNIMED', 'CENTRAL NACIONAL UNIMED'),
('INTEGRAL SAÚDE', 'INTEGRAL SAÚDE'),
('CIGNA', 'CIGNA'),
('UNIMED ARARUAMA ', 'UNIMED ARARUAMA '),
('CNEN', 'CNEN'),
('HOSPITAÚITAUSEG SAÚDE SA', 'HOSPITAÚITAUSEG SAÚDE SA'),
('HOSPITAÚ', 'HOSPITAÚ'),
('ELETROS', 'ELETROS'),
('CAMPERJ', 'CAMPERJ'),
('INTEGRAL SAÚDE', 'INTEGRAL SAÚDE'),
('TEST', 'TEST'),
('UNIMED SEGUROS', 'UNIMED SEGUROS'),
('CARE PLUS', 'CARE PLUS'),
('AMAFRERJ', 'AMAFRERJ'),
('VALE/PASA', 'VALE/PASA'),
('CASSI', 'CASSI'),
('PREVENT SENIOR', 'PREVENT SENIOR'),
('CNEN', 'CNEN'),
('FIOSAÚDE', 'FIOSAÚDE'),
('EMBRATELPRIMESYS', 'EMBRATELPRIMESYS'),
('EMBRATELSTAR ONE S/A', 'EMBRATELSTAR ONE S/A'),
('EMBRATELTELMEX', 'EMBRATELTELMEX'),
('EMBRATELTVSAT', 'EMBRATELTVSAT'),
('ELETROS', 'ELETROS'),
('BRADESCO S.A.', 'BRADESCO S.A.'),
('GAMA SAÚDE', 'GAMA SAÚDE'),
('CAPESESP', 'CAPESESP'),
('SOMPO SEGUROS SAUDE S/A', 'SOMPO SEGUROS SAUDE S/A'),
('AMIL', 'AMIL'),
('TASY', 'TASY'),
('CABERJ', 'CABERJ'),
('CAPESESP', 'CAPESESP'),
('CENTRAL NACIONAL UNIMED', 'CENTRAL NACIONAL UNIMED'),
('EMBRATELSTAR ONE S/A', 'EMBRATELSTAR ONE S/A'),
('EMBRATELTVSAT TELECOMUNICAÇÕES', 'EMBRATELTVSAT TELECOMUNICAÇÕES'),
('EMBRATELTELMEX DO BRASIL', 'EMBRATELTELMEX DO BRASIL'),

)

HOSPITAL = (
('Hospital Barra DOr', 'Hospital Barra DOr'),
('Hospital Pasteur', 'Hospital Pasteur'),
('Hospital Samaritano Barra', 'Hospital Samaritano Barra'),
('Hospital Samaritano Botafogo', 'Hospital Samaritano Botafogo'),
('Hospital Evangélico', 'Hospital Evangélico'),
('Hospital Quinta DOr', 'Hospital Quinta DOr'),
('Hospital São Vicente de Paulo', 'Hospital São Vicente de Paulo'),
('Hospital Copa DOr', 'Hospital Copa DOr'),
('HCN_CHN', 'HCN_CHN'),
('Casa de Saúde São José', 'Casa de Saúde São José'),
('Hospital Assim Méier', 'Hospital Assim Méier'),
('Hospital Copa Star', 'Hospital Copa Star'),
('Hospital Vitória Barra', 'Hospital Vitória Barra'),
('Hospital Pró-Cardíaco', 'Hospital Pró-Cardíaco'),
('Hospital São Lucas', 'Hospital São Lucas'),
('Hospital das Américas', 'Hospital das Américas'),
('Hospital Badim', 'Hospital Badim'),
('Hospital Silvestre', 'Hospital Silvestre'),
('Hospital Mário Lioni', 'Hospital Mário Lioni'),
('Hospital Placi Niterói', 'Hospital Placi Niterói'),
('Hospital Israelita', 'Hospital Israelita'),
('Hospital de Clínicas de Jacarepaguá', 'Hospital de Clínicas de Jacarepaguá'),
('Hospital São Vicente da Gávea', 'Hospital São Vicente da Gávea'),
('Hospital Espanhol', 'Hospital Espanhol'),
('Hospital Mário Kroeff', 'Hospital Mário Kroeff'),
('Hospital Dr Balbino', 'Hospital Dr Balbino'),
('Hospital Norte DOr', 'Hospital Norte DOr'),
('Hospital Icaraí', 'Hospital Icaraí'),
('Hospital Panamericano', 'Hospital Panamericano'),
('Hospital Niterói DOr', 'Hospital Niterói DOr'),
('Hospital Rio Laranjeiras', 'Hospital Rio Laranjeiras'),
('Hospital e Clínica São Gonçalo', 'Hospital e Clínica São Gonçalo'),
('Clinicare', 'Clinicare'),
('Hospital Ordem Terceira ', 'Hospital Ordem Terceira '),
('Hospital Sírio Libanês', 'Hospital Sírio Libanês'),
('Hospital Rios DOr', 'Hospital Rios DOr'),
('Hospital Bela Lopes', 'Hospital Bela Lopes'),
('Casa de Saúde Pinheiro Machado', 'Casa de Saúde Pinheiro Machado'),
('Hospital Santa Marta', 'Hospital Santa Marta'),
('Hospital Caxias DOr', 'Hospital Caxias DOr'),
('Hospital Ingá', 'Hospital Ingá'),
('Hospital Alameda Niterói', 'Hospital Alameda Niterói'),
('Hospital Casa de Portugal', 'Hospital Casa de Portugal'),
('Hospital e Maternidade Santa Lúcia', 'Hospital e Maternidade Santa Lúcia'),
('Casa de Repouso_Asilo', 'Casa de Repouso_Asilo'),
('Residência', 'Residência'),
('Home Care', 'Home Care'),
('Pronto Socorro', 'Pronto Socorro'),
('Consultório', 'Consultório'),
('Outro Hospital', 'Outro Hospital'),
('Hospital Quali Ipanema', 'Hospital Quali Ipanema'),
('Hospital de Nova Iguaçu', 'Hospital de Nova Iguaçu'),
('Hospital Oeste Dor', 'Hospital Oeste Dor'),
('Hospital Rio Mar', 'Hospital Rio Mar'),
('Hospital Municipal Salgado Filho', 'Hospital Municipal Salgado Filho'),
('Hospital Santa Tereza', 'Hospital Santa Tereza'),
('Hospital Albert Einstein (SP)', 'Hospital Albert Einstein (SP)'),
('Hospital Oswaldo Cruz (SP)', 'Hospital Oswaldo Cruz (SP)'),
('Hospital NIG Barra', 'Hospital NIG Barra'),
('Hospital Vital', 'Hospital Vital'),
('Hospital Placi Niteroi', 'Hospital Placi Niteroi'),
('Hospital Placi Botafogo', 'Hospital Placi Botafogo'),

)

STATUS_HORA_MEDICACAO = (
    ('Primeiro:', 'de 4 em 4 horas'),
    ('Segundo:', '8 em 8 horas'),
    ('Terceiro:', '12 em 12 horas'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_DOENCA_BASE = (
('Z93.1', 'GASTROSTOMIA'),
('Z93.0', 'TRAQUEOSTOMIA'),
('F03  ', 'DEMENCIA NE'),
('E14  ', 'DIABETES MELLITUS NE'),
('L89  ', 'ULCERA DE DECUBITO'),
('F00  ', 'DEMENCIA NA DOENC DE ALZHEIMER'),
('J44.9', 'DOENC PULMONAR OBSTRUTIVA CRONICA NE'),
('Z43.0', 'CUIDADOS A TRAQUEOSTOMIA'),
('N18  ', 'INSUF RENAL CRONICA'),
('E03.9', 'HIPOTIREOIDISMO NE'),
('I69.3', 'SEQUELAS DE INFARTO CEREBRAL'),
('E10  ', 'DIABETES MELLITUS INSULINO-DEPENDENTE'),
('E11  ', 'DIABETES MELLITUS NAO-INSULINO-DEPENDEMTE'),
('I63  ', 'INFARTO CEREBRAL'),
('G20  ', 'DOENC DE PARKINSON'),
('G30  ', 'DOENC DE ALZHEIMER'),
('F01  ', 'DEMENCIA VASCULAR'),
('I48  ', 'FLUTTER E FIBRILACAO ATRIAL'),
('I64  ', 'ACID VASC CEREBR NE COMO HEMORRAG ISQUEMICO'),
('Z43.1', 'CUIDADOS A GASTROSTOMIA'),
('OUTRO', 'OUTRAS DOENÇAS'),

)

STATUS_FEBRE = (
    ('FEBRE', '38'),
    ('FEBRIL', '37.4<38'),
    ('FEBRIL', '37.0'),
    ('NORMAL', 'ABAIXO 37.0'),
    ('OUTROS', 'OUTROS VALORES'),
    
)

STATUS_GLICEMIA = (
    ('Normal:', 'Normal: inferior a 99 mg/dL'),
    ('Pré-diabetes:', 'Pré-diabetes: entre 100 e 125 mg/dL'),
    ('Diabetes:', 'Diabetes: superior a 126 mg/dL em dois dias diferentes'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_CARDIO = (
    ('Primeiro:', 'Bradicardia 10 a 50 bpm'),
    ('Segundo:', 'Normal 60 a 100 bpm'),
    ('Terceiro:', 'Taquicardia 110 a 140'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_PRECAUCAO = (
    ('SIM:', 'SIM'),
    ('NAO:', 'NÃO'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_BRADEN = (
('BAIXO:', '15 Risco baixo'),
('BAIXO:', '16 Risco baixo'),
('BAIXO:', '17 Risco baixo'),
('BAIXO:', '>= 18 Risco baixo'),
('BAIXO:', '16 Risco baixo'),
('MODERADO:', '13 Risco moderado'),
('MODERADO:', '14 Risco moderado'),
('ALTO:', '10 Risco alto'),
('ALTO:', '11 Risco alto'),
('ALTO:', '12 Risco alto'),
('MUITO_ALTO:', '<= 9 Risco muito alto'),
('NORMAL', 'OUTROS VALORES'),

)

    

class DadosPaciente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    comentarios = models.TextField(blank=True, null=True,verbose_name="Comentarios")
    medico = models.CharField(verbose_name="Nome Medico", max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
    convenios = models.CharField(verbose_name="Convênios", choices=STATUS_CONVENIOS, max_length=200, blank=True, null=True)
    hospital = models.CharField(verbose_name="Hospital",choices=HOSPITAL, max_length=100, blank=True, null=True)
    criacao = models.DateTimeField(auto_now_add=True)
    sinal_febre = models.CharField(max_length=30, choices=STATUS_FEBRE, default='NORMAL')
    alergia = models.NullBooleanField(verbose_name="Alergico?")
    glicemia = models.CharField(max_length=30, choices=STATUS_GLICEMIA, default='NORMAL')
    frequencia_cardiaca = models.CharField(max_length=30, choices=STATUS_CARDIO, default='NORMAL')
    cid = models.CharField(verbose_name="Doença Base",choices=STATUS_DOENCA_BASE, max_length=100, blank=True, null=True)
    peso = models.CharField(verbose_name="Peso", max_length=30, blank=True, null=True)
    altura = models.DecimalField(verbose_name="Altura", max_digits=5, decimal_places=2, blank=True, null=True)
    medicamento = models.CharField(verbose_name="Medicamento", max_length=200, blank=True, null=True)
    horarios_medicacao = models.CharField(max_length=30, choices=STATUS_HORA_MEDICACAO, default='NORMAL') 
    idade = models.IntegerField(null=True)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Feminino')), null=True)
    precaucao = models.IntegerField(choices=((1, 'SIM'), (2, 'NÃO')), null=True, verbose_name="PRECAUÇÃO")
    banho_leito = models.IntegerField(choices=((1, 'SIM'), (2, 'NÃO')), null=True, verbose_name="BANHO NO LEITO")
    Braden = models.CharField(max_length=30, choices=STATUS_BRADEN, default='NORMAL')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.nome



class Medicamentos(models.Model):
    medicamento = models.CharField(max_length=200, blank=True, null=True)
    sub_grupo = models.CharField(max_length=200, blank=True, null=True)
    un_medida = models.CharField(verbose_name="Unidade de Medida", max_length=10, blank=True, null=True)
    medicamento_import = models.FileField(blank=True, null=True, upload_to='media/')
    paciente = models.ForeignKey(DadosPaciente, on_delete = models.SET_NULL, blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


    
    def __str__(self):
        return self.medicamento