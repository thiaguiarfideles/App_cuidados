from django.db import models
from usuarios.models import User
from core.helpers import validate_CPF, validate_file_extension


def identidade_frente_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.ds_codigo_conselho, "id_frente_"+filename)

def identidade_verso_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.ds_codigo_conselho, "id_verso_"+filename)
def comp_resid_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.ds_codigo_conselho, "comp_resid_"+filename)

def comp_cnpj_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.ds_codigo_conselho, "comp_cnpj_"+filename)


class Especialidade(models.Model):
    nm_especialidade = models.CharField(blank=False, max_length=100)
    def __str__(self):
        return self.nm_especialidade

STATUS_CADASTRO = (
    ('PENDENTE', 'Aguardando Validação'),
    ('VALIDADO', 'Validado (Ativo)'),
    ('INVALIDO', 'Inválido'),
    ('INATIVO', 'Inativo'),
)

STATUS_CADASTRO = (
    ('PENDENTE', 'Aguardando Validação'),
    ('VALIDADO', 'Validado (Ativo)'),
    ('INVALIDO', 'Inválido'),
    ('INATIVO', 'Inativo'),

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

STATUS_HORA_MEDICACAO = (
    ('Primeiro:', 'de 4 em 4 horas'),
    ('Segundo:', '8 em 8 horas'),
    ('Terceiro:', '12 em 12 horas'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_CARDIO = (
    ('Primeiro:', 'Bradicardia 10 a 50 bpm'),
    ('Segundo:', 'Normal 60 a 100 bpm'),
    ('Terceiro:', 'Taquicardia 110 a 140'),
    ('NORMAL', 'OUTROS VALORES'),
    
)

STATUS_ALERGIA = (
    ('Primeiro:', 'LEVE'),
    ('Segundo:', 'GRAVE'),
    ('Terceiro:', 'MODERADO'),
    ('Quarto:', 'Não Alergico'),
    ('NORMAL', 'OUTROS VALORES'),
    
)
    

STATUS_HOSPITAL = (
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

STATUS_CONVENIO = (
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
    

class PrestadorPessoaFisica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    status=models.CharField(max_length=30, choices=STATUS_CADASTRO, default='PENDENTE')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ##dado que precisa ser tirado do sistema
    cd_prestador = models.IntegerField(unique=False,blank=True, null=True)
    sn_cuidador = models.NullBooleanField(verbose_name="Cuidador?")
    sn_paciente = models.NullBooleanField(verbose_name="Paciente?")
    nm_prestador = models.CharField(verbose_name="Nome Completo", max_length=100)
    nr_cpf_cgc = models.CharField(verbose_name="CPF",max_length=11,validators=[validate_CPF])
    medico_responsavel = models.CharField(verbose_name="Nome Medico Responsável", max_length=100, blank=True, null=True)
    hospital_referencia = models.CharField(verbose_name="Hospital de Referência",choices=STATUS_HOSPITAL, max_length=100, blank=True, null=True)
    convenio = models.CharField(verbose_name="Convênio", choices=STATUS_CONVENIO, max_length=200, blank=True, null=True)
    doenca_base = models.CharField(verbose_name="Doença Base",choices=STATUS_DOENCA_BASE, max_length=100, blank=True, null=True)
    medicamento = models.CharField(verbose_name="Medicamento", max_length=200, blank=True, null=True)
    horarios_medicacao = models.CharField(max_length=30, choices=STATUS_HORA_MEDICACAO, default='NORMAL')    
    peso = models.CharField(verbose_name="Peso", max_length=30, blank=True, null=True)
    altura = models.CharField(verbose_name="Altura", max_length=30, blank=True, null=True)
    temperatura = models.CharField(max_length=30, choices=STATUS_FEBRE, default='NORMAL')
    glicemia = models.CharField(max_length=30, choices=STATUS_GLICEMIA, default='NORMAL')
    frequencia_cardiaca = models.CharField(max_length=30, choices=STATUS_CARDIO, default='NORMAL')
    alergia = models.NullBooleanField(verbose_name="Alergico?")
    tipo_alergia = models.CharField(verbose_name="Tipo de Alergia", max_length=100, blank=True, null=True)
    nivel_alergia = models.CharField(max_length=30, choices=STATUS_ALERGIA, default='NORMAL')
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)
    nm_mae = models.CharField(verbose_name="Nome da Mãe", max_length=100)
    nm_pai = models.CharField(verbose_name="Nome do Pai", max_length=100,blank=True, null=True)
    ds_codigo_conselho = models.CharField(verbose_name="Código do Conselho", max_length=10,blank=True, null=True)
    ds_faculdade = models.CharField(verbose_name="Nome da Faculdade", max_length=200,blank=True, null=True)
    ds_email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    nr_cep = models.CharField(verbose_name="CEP", max_length=8,blank=True, null=True)
    ds_endereco = models.CharField(verbose_name="Endereço", max_length=200, blank=True, null=True)
    ds_complemento = models.CharField(verbose_name="Complemento", max_length=20, blank=True, null=True)
    ds_bairro = models.CharField(verbose_name="Bairro", max_length=200, blank=True, null=True)
    nm_cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
    cd_uf = models.CharField(verbose_name="UF", max_length=200, blank=True, null=True)
    banco = models.CharField(max_length=50,blank=True, null=True)
    ds_agencia = models.CharField(verbose_name="Agência Bancária", max_length=20, blank=True, null=True)
    nr_conta = models.CharField(verbose_name="Conta Bancária", max_length=20,blank=True, null=True)
    nr_fone_contato = models.CharField(verbose_name="Telefone para Contato", max_length=20,blank=True, null=True)
    # nr_fone_comercial = models.CharField(max_length=200,blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True,verbose_name="Observações")
    data_insercao = models.DateTimeField(auto_now_add=True)
    identidade_frente =models.FileField(verbose_name="Enviar Imagem 1",upload_to=identidade_frente_directory_path,validators=[validate_file_extension])
    identidade_verso = models.FileField(verbose_name="Enviar Imagem 2",upload_to=identidade_verso_directory_path,validators=[validate_file_extension])
    comprovante_residencia = models.FileField(verbose_name="Enviar Imagem 3",upload_to=comp_resid_directory_path,validators=[validate_file_extension])
    especialidades = models.ManyToManyField(Especialidade)

    # nm_completo = models.CharField(verbose_name="Nome Completo", max_length=100)
    # ##dado que precisa ser tirado do sistema
    # cd_fornecedor = models.IntegerField(verbose_name="Código Fornecedor MV", default=0, unique=False,blank=True, null=True)
    # nm_fornecedor = models.CharField(verbose_name="Razão Social", max_length=200,blank=True, null=True)
    # nm_fantasia= models.CharField(verbose_name="Nome Fantasia", max_length=200,blank=True, null=True)
    ##novamente, campo precisa de validação do sistema
    # nm_tip_presta = models.CharField(verbose_name="Tipo de Prestador",max_length=200, blank=True, null=True)
    # comprovante_cnpj = models.FileField(upload_to=comp_cnpj_directory_path)

    class Meta:
        verbose_name_plural = "prestadores"


