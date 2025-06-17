# %%
from dash import html, dcc, Dash, Input, Output,callback
from dash.dependencies import Input, Output
import CriarMapaFolium 
import pandas as pd


# %%
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# %%



app = Dash(__name__)

sexo = {'1':'Homem','2':'Mulher','9':'Sem resposta'}
idade = {'1':'Menos de 13 anos','2':'13 a 15 anos','3':'16 ou 17 anos','4':'18 anos ou mais','9':'Sem resposta'}
nascimento = {'-2':'Abandono de questionário','2000':'Antes de 2001','2001':'2001','2002':'2002','2003':'2003','2004':'2004','2005':'2005','2006':'2006','2007':'2007','2008':'2008 ou mais','9999':'Sem resposta'}
corRaca = {'-2':'Abandono de questionário','1':'Branca','2':'Preta','3':'Amarela','4':'Parda','5':'Indígena','9':'Sem resposta'}
anoEscolar = {'-2':'Abandono de questionário','1':'6º ano do Ensino Fundamental','2':'7º ano do Ensino Fundamental','3':'8º ano do Ensino Fundamental','4':'9º ano do Ensino Fundamental','5':'1º ano do Ensino Médio','6':'2º ano do Ensino Médio','7':'3º ano do Ensino Médio','8':'Sem resposta'}
pessoasPorCasa = {'-2':'Abandono de questionário','1':'1 pessoa (moro sozinho)','2':'2 pessoas','3':'3 pessoas','4':'4 pessoas','5':'5 pessoas','6':'6 pessoas','7':'7 pessoas','8':'8 pessoas','9':'9 pessoas','10':'10 pessoas ou mais','99':'Sem resposta'}
esferaAdministrativa = {'1':'Federal','2':'Estadual','3':'Municipal','4':'Privada'}


dados = ['Alimentação','Atividade Fisica','Situações em casa e na escola','Saúde mental','Saúde sexual e reprodutiva','Higiene e saúde bucal','Uso de serviço de saúde']

Perguntas = {}

perguntasResumidas = {

    "B02019A": 'Você toma café da manhã?',
    "B02017A": 'Você almoça/janta com sua família?',
    "B02018B": 'Você come assistindo TV ou mexendo no celular?',
    "B02028": 'Ontem, você tomou refrigerante?',
    "B02029": 'Ontem, tomou suco de caixinha/lata?',
    "B02030": 'Ontem, tomou refresco em pó?',
    "B02031": 'Ontem, tomou bebida achocolatada?',
    "B02032": 'Ontem, tomou iogurte com sabor?',
    "B02033": 'Ontem, comeu salgadinho ou biscoito salgado?',
    "B02034": 'Ontem, comeu biscoito doce/recheado ou bolinho?',
    "B02035": 'Ontem, comeu chocolate, sorvete ou sobremesa industrializada?',
    "B02036": 'Ontem, comeu salsicha, linguiça, mortadela ou presunto?',
    "B02037": 'Ontem, comeu pão de forma ou pão de hambúrguer?',
    "B02038": 'Ontem, comeu margarina?',
    "B02039": 'Ontem, comeu maionese, ketchup ou molhos?',
    "B02040": 'Ontem, comeu miojo, sopa de pacote ou comida congelada?',
    "B02001": 'Nos últimos 7 dias, quantos dias comeu feijão?',
    "B02004B": 'Nos últimos 7 dias, comeu legumes/verduras sem ser batata ou mandioca?',
    "B02010A": 'Nos últimos 7 dias, quantos dias comeu guloseimas?',
    "B02011": 'Nos últimos 7 dias, quantos dias comeu frutas?',
    "B02013": 'Nos últimos 7 dias, quantos dias tomou refrigerante?',
    "B02023A": 'Nos últimos 7 dias, quantos dias comeu em lanchonetes/fast food?',
    "B02021A": 'Sua escola oferece merenda gratuita?',
    "B02020B": 'Você come a merenda da escola?',
    "B02041": 'Você compra comida na cantina?',
    "B02042": 'Você compra comida de ambulantes na porta da escola?',
    "B03001A1": 'Nos últimos 7 dias, quantos dias foi a pé/bicicleta para a escola?',
    "B03002A1": 'Quando vai a pé/bicicleta, quanto tempo gasta?',
    "B03001A2": 'Nos últimos 7 dias, quantos dias voltou a pé/bicicleta da escola?',
    "B03002A2": 'Quando volta a pé/bicicleta, quanto tempo gasta?',
    "B03003A": 'Nos últimos 7 dias, quantos dias teve aula de educação física?',
    "B03005B": 'Quanto tempo duraram suas aulas práticas de educação física?',
    "B03006B": 'Nos últimos 7 dias, quantos dias praticou atividade física fora da escola?',
    "B03007A": 'Quanto tempo por dia duraram essas atividades?',
    "B03009B": 'Quantas horas por dia você assiste TV? (Exceto fim de semana/feriados)',
    "B03010B": 'Quantas horas por dia passa sentado(a) em telas? (Exceto fim de semana/feriados)',
    "B07001": 'Nos últimos 30 dias, quantos dias faltou à escola sem permissão?',
    "B07002": 'Nos últimos 30 dias, seus responsáveis sabiam o que você fazia no tempo livre?',
    "B07004": 'Nos últimos 30 dias, seus responsáveis entenderam seus problemas e preocupações?',
    "B07006": 'Nos últimos 30 dias, com que frequência seus colegas o trataram bem e foram prestativos?',
    "B07007A": 'Nos últimos 30 dias, quantas vezes colegas zombaram de você a ponto de magoá-lo?',
    "B07008": 'Nos últimos 30 dias, por que colegas zombaram ou humilharam você?',
    "B07011": 'Nos últimos 30 dias, quantas vezes colegas o isolaram sem motivo?',
    "B07012": 'Nos últimos 30 dias, quantas vezes colegas agrediram fisicamente você?',
    "B07013": 'Nos últimos 30 dias, você se sentiu ameaçado ou humilhado nas redes sociais?',
    "B07009": 'Nos últimos 30 dias, você zombou ou humilhou algum colega?',
    "B12003": 'Quantos amigos próximos você tem?',
    "B12004": 'Nos últimos 30 dias, com que frequência você se preocupou com tarefas ou atividades?',
    "B12005": 'Nos últimos 30 dias, com que frequência você se sentiu triste?',
    "B12006": 'Nos últimos 30 dias, com que frequência sentiu que ninguém se preocupa com você?',
    "B12007": 'Nos últimos 30 dias, com que frequência se sentiu irritado, nervoso ou mal-humorado?',
    "B12008": 'Nos últimos 30 dias, com que frequência sentiu que a vida não vale a pena?',
    "B08001":'Você já teve relação sexual?',
    "B08002":'Com quantos anos foi sua primeira relação sexual?',
    "B08011A":'Você ou seu parceiro usou camisinha na primeira vez?',
    "B08006A":'Na última vez, você ou seu parceiro usou camisinha?',
    "B08014":'Como conseguiu a camisinha na última vez?',
    "B08007":'Na última vez, usou outro método para evitar gravidez?',
    "B08012A":'Qual método usou para evitar gravidez na última vez?',
    "B08015":'Você ou sua parceira já usou pílula do dia seguinte?',
    "B08016":'Como conseguiu a pílula do dia seguinte na última vez?',
    "B08013A":'Você já engravidou ou engravidou alguém?',
    "B08008A":'Já recebeu orientação sobre prevenção de gravidez na escola?',
    "B08009A":'Já recebeu orientação sobre prevenção de DSTs na escola?',
    "B08010A":'Já recebeu orientação sobre como conseguir camisinha grátis?',
    "B10004A": "Com que frequência você lava as mãos antes de comer?",
    "B10005A": "Com que frequência você lava as mãos após usar o banheiro?",
    "B10006A": "Você usa sabão ao lavar as mãos?",
    "B10001B": "Quantas vezes por dia você escova os dentes?",
    "B10002": "Nos últimos 6 meses, teve dor de dente (sem ser por aparelho)?",
    "B10003": "Nos últimos 12 meses, quantas vezes foi ao dentista?",
    "B13005":'Como você classifica sua saúde?',
    "B13006":'Nos últimos 12 meses, quantos dias faltou à escola por motivo de saúde?',
    "B13001":'Nos últimos 12 meses, procurou atendimento médico?',
    "B13002A":'Qual serviço de saúde você mais procurou nos últimos 12 meses?',
    "B13003A":'Quantas vezes buscou uma Unidade Básica de Saúde nos últimos 12 meses?',
    "B13004B":'Foi atendido na última vez que procurou a Unidade Básica de Saúde?',
    "B13007A":'Qual foi o principal motivo da sua última consulta na Unidade Básica de Saúde?',
    "B13009A":'Você foi vacinado(a) contra o HPV?',
    "B13012":'Por que não tomou a vacina contra o HPV?'

}

alimentacao = {
    "B02019A": "Você costuma tomar o café da manhã?",
    "B02017A": "Você costuma almoçar ou jantar com sua mãe, pai ou responsável?",
    "B02018B": "Nas suas refeições, com que frequência você costuma comer fazendo alguma outra coisa (assistindo à TV, mexendo no computador ou no celular)?",
    "B02028": "ONTEM, você tomou refrigerante?",
    "B02029": "ONTEM, você tomou suco de fruta em caixinha ou lata?",
    "B02030": "ONTEM, você tomou refresco em pó?",
    "B02031": "ONTEM, você tomou bebida achocolatada?",
    "B02032": "ONTEM, você tomou iogurte com sabor?",
    "B02033": "ONTEM, você comeu salgadinho de pacote (chips) ou biscoito/bolacha salgado?",
    "B02034": "ONTEM, você comeu biscoito ou bolacha doce, biscoito recheado ou bolinho de pacote?",
    "B02035": "ONTEM, você comeu chocolate, sorvete, gelatina, flan ou outra sobremesa industrializada?",
    "B02036": "ONTEM, você comeu salsicha, linguiça, mortadela ou presunto?",
    "B02037": "ONTEM, você comeu pão de forma, pão de cachorro-quente ou pão de hambúrguer?",
    "B02038": "ONTEM, você comeu margarina?",
    "B02039": "ONTEM, você comeu maionese, ketchup ou outros molhos industrializados?",
    "B02040": "ONTEM, você comeu macarrão instantâneo (miojo), sopa de pacote, lasanha congelada ou outro prato pronto comprado congelado?",
    "B02001": "NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu feijão?",
    "B02004B": "NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu pelo menos um tipo de legume ou verdura que não seja batata ou aipim (mandioca/macaxeira)?",
    "B02010A": "NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu guloseimas doces, como balas, confeitos, chocolates, chicletes, bombons, pirulitos e outros?",
    "B02011": "NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu frutas frescas ou salada de frutas?",
    "B02013": "NOS ÚLTIMOS 7 DIAS, em quantos dias você tomou refrigerante?",
    "B02023A": "NOS ÚLTIMOS 7 DIAS, em quantos deles você comeu em lanchonetes, barracas de cachorro quente, pizzaria, fast food etc?",
    "B02021A": "Sua escola oferece comida/merenda aos alunos da sua turma? (Não considerar comida comprada na cantina)",
    "B02020B": "Você costuma comer a comida/merenda oferecida pela escola? (Não considerar comida comprada na cantina)",
    "B02041": "Você costuma comprar alimentos ou bebidas na cantina dentro da escola? (Não considerar a compra de água)",
    "B02042": "Você costuma comprar alimentos ou bebidas de vendedores de rua (camelô ou ambulante) na porta ou ao redor da escola? (Não considerar a compra de água)"
}
atividadeFisica = {
    "B03001A1": "NOS ÚLTIMOS 7 DIAS, em quantos dias você FOI a pé ou de bicicleta para a escola?",
    "B03002A1": "Quando você VAI para a escola a pé ou de bicicleta, quanto tempo você gasta?",
    "B03001A2": "NOS ÚLTIMOS 7 DIAS, em quantos dias você VOLTOU a pé ou de bicicleta da escola?",
    "B03002A2": "Quando você VOLTA da escola a pé ou de bicicleta, quanto tempo você gasta?",
    "B03003A": "NOS ÚLTIMOS 7 DIAS, quantos dias você TEVE aulas de educação física na escola?",
    "B03005B": "Quanto tempo por dia você FEZ atividade física ou praticou esporte durante as aulas de educação física na escola? Não considere o tempo gasto em atividades teóricas em sala de aula.",
    "B03006B": "NOS ÚLTIMOS 7 DIAS, sem contar as aulas de educação física da escola, em quantos dias você praticou alguma atividade física?",
    "B03007A": "Quanto tempo por dia duraram essas atividades que você fez?",
    "B03009B": "Quantas horas por dia você assiste a televisão (TV)? (NÃO contar sábado, domingo e feriado)",
    "B03010B": "Quantas horas por dia você costuma ficar sentado(a), assistindo televisão, jogando videogame, usando computador, celular, tablet ou fazendo outras atividades sentado(a)? (NÃO contar sábado, domingo, feriados ou o tempo sentado na escola)"
}
situacoesCasaEscola = {
    "B07001": "NOS ÚLTIMOS 30 DIAS, em quantos dias você faltou às aulas ou à escola sem permissão de sua mãe, pai ou responsável?",
    "B07002": "NOS ÚLTIMOS 30 DIAS, com que frequência sua mãe, pai ou responsável sabia realmente o que você estava fazendo em seu tempo livre?",
    "B07004": "NOS ÚLTIMOS 30 DIAS, com que frequência sua mãe, pai ou responsável entendeu seus problemas e preocupações?",
    "B07006": "NOS ÚLTIMOS 30 DIAS, com que frequência os colegas de sua escola trataram você bem e/ou foram prestativos com você?",
    "B07007A": "NOS ÚLTIMOS 30 DIAS, quantas vezes algum dos seus colegas de escola o esculachou, zoou, mangou, intimidou ou caçoou tanto que você ficou magoado, incomodado, aborrecido, ofendido ou humilhado?",
    "B07008": "NOS ÚLTIMOS 30 DIAS, qual o motivo/causa de seus colegas terem esculachado, zombado, zoado, caçoado, mangado, intimidado ou humilhado?",
    "B07011": "NOS ÚLTIMOS 30 DIAS, quantas vezes algum dos seus colegas de escola se recusou a falar com você, deixou você de lado sem razão ou fez com que outros colegas deixassem de falar com você?",
    "B07012": "NOS ÚLTIMOS 30 DIAS, quantas vezes algum dos seus colegas de escola bateu (deu socos, tapas, chutes, pontapés) em você ou o machucou fisicamente de outra forma?",
    "B07013": "NOS ÚLTIMOS 30 DIAS, você se sentiu ameaçado(a), ofendido(a) ou humilhado(a) nas redes sociais ou aplicativos de celular?",
    "B07009": "NOS ÚLTIMOS 30 DIAS, você esculachou, zombou, mangou, intimidou ou caçoou algum de seus colegas da escola tanto que ele ficou magoado, aborrecido, ofendido ou humilhado?"
}
saudeMental = {
    "B12003": "Quantos(as) amigos(as) próximos você tem?",
    "B12004": "NOS ÚLTIMOS 30 DIAS, com que frequência você se sentiu muito preocupado com as coisas comuns do seu dia a dia como atividades da escola, competições esportivas, tarefas de casa, etc.?",
    "B12005": "NOS ÚLTIMOS 30 DIAS, com que frequência você se sentiu triste?",
    "B12006": "NOS ÚLTIMOS 30 DIAS, com que frequência você sentiu que ninguém se preocupa com você?",
    "B12007": "NOS ÚLTIMOS 30 DIAS, com que frequência você se sentiu irritado(a), nervoso(a) ou mal-humorado(a) por qualquer coisa?",
    "B12008": "NOS ÚLTIMOS 30 DIAS, com que frequência você sentiu que a vida não vale a pena ser vivida?"
}

saudeReprodutiva = {
    "B08001": "Você já teve relação sexual (transou) alguma vez?",
    "B08002": "Que idade você tinha quando teve relação sexual (transou) pela primeira vez?",
    "B08011A": "Você ou seu(sua) parceiro(a) usou camisinha (preservativo) NA PRIMEIRA RELAÇÃO SEXUAL?",
    "B08006A": "NA ÚLTIMA VEZ que você teve relação sexual (transou), você ou seu(sua) parceiro(a) usou camisinha (preservativo)?",
    "B08014": "Nesta última vez que você teve relação sexual (transou), como você conseguiu a camisinha (preservativo)?",
    "B08007": "NA ÚLTIMA VEZ que você teve relação sexual (transou), você ou seu(sua) parceiro(a) usou algum outro método para evitar a gravidez que não seja camisinha (preservativo)?",
    "B08012A": "Nesta última vez que você teve relação sexual (transou), qual outro método você ou seu(sua) parceiro(a) usou para evitar gravidez?",
    "B08015": "Alguma vez na vida, você ou sua parceira já usou pílula do dia seguinte (contracepção de emergência)?",
    "B08016": "NA ÚLTIMA VEZ que você ou sua parceira usou pílula do dia seguinte (contracepção de emergência) como conseguiu?",
    "B08013A": "Alguma vez na vida você engravidou, mesmo que a gravidez não tenha chegado ao fim?",
    "B08008A": "Na escola, você já recebeu orientação sobre prevenção de gravidez?",
    "B08009A": "Na escola, você já recebeu orientação sobre prevenção de HIV/AIDS ou outras Doenças/Infecções Sexualmente Transmissíveis?",
    "B08010A": "Na escola, você já recebeu orientação sobre como conseguir camisinha (preservativo) gratuitamente?"
}
higiene = {
    "B10004A": "Com que frequência você lava as mãos antes de comer?",
    "B10005A": "Com que frequência você lava as mãos após usar o banheiro ou o vaso sanitário?",
    "B10006A": "Com que frequência você usa sabão ou sabonete quando lava suas mãos?",
    "B10001B": "Quantas vezes por dia você escova os dentes?",
    "B10002": "NOS ÚLTIMOS 6 MESES, você teve dor de dente que não tenha sido causada por uso de aparelho?",
    "B10003": "NOS ÚLTIMOS 12 MESES, quantas vezes você foi ao dentista?"
}

usoSaude = {
    "B13005": "Como você classificaria seu estado de saúde?",
    "B13006": "NOS ÚLTIMOS 12 MESES, quantos dias você faltou a escola por motivo(s) relacionado(s) à própria saúde?",
    "B13001": "NOS ÚLTIMOS 12 MESES você procurou algum serviço ou profissional de saúde para atendimento relacionado à própria saúde?",
    "B13002A": "NOS ÚLTIMOS 12 MESES, qual foi o serviço de saúde que você procurou com MAIS FREQUÊNCIA?",
    "B13003A": "NOS ÚLTIMOS 12 MESES, quantas vezes você procurou por alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF)?",
    "B13004B": "Você foi atendido NA ÚLTIMA VEZ que procurou alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF)?",
    "B13007A": "Qual foi o PRINCIPAL MOTIVO da sua procura na Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF) NESTA ÚLTIMA VEZ?",
    "B13009A": "Você foi vacinado(a) contra o vírus HPV?",
    "B13012": "Por que você não foi vacinado(a) contra o vírus HPV?"
}

Perguntas.update(alimentacao)
Perguntas.update(atividadeFisica)
Perguntas.update(situacoesCasaEscola)
Perguntas.update(saudeMental)
Perguntas.update(saudeReprodutiva)
Perguntas.update(higiene)
Perguntas.update(usoSaude)

sexo_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in sexo.items()]
alimentacao_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in alimentacao.items()]
atividade_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in atividadeFisica.items()]
situacoesCasaEscola_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in situacoesCasaEscola.items()]
saudeMental_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in saudeMental.items()]
saudeReprodutiva_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in saudeReprodutiva.items()]
higiene_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in higiene.items()]
usoSaude_checklist = [{"label": pergunta, "value": codigo} for codigo, pergunta in usoSaude.items()]

listSglEstados = ['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','PAL','FLO','CUR','SAP','BLH','RDJ','VIT','CGE','GOI','DIF','SAL','CUI','PTV','ROB','PAS','ARC','MCO','RCF','JPS','NTL','FRT','SLS','BLM','MCP','BOA','MNS','TRS']

UF = [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52]
codCap = [4314902,4205407,4106902,3550308,3106200,3304557,3205309,5002704,5208707,5300108,2927408,5103403,1100205,1200401,1721000,2800308,2704302,2611606,
          2507507,2408102,2304400,2111300,1501402,1600303,1400100,1302603,2211001]


# %%


app.layout = html.Div(className='telaMapa',children=[
    # Div principal com display flex para colocar os dropdowns e o mapa lado a lado
        # Coluna dos Dropdowns
    
    html.Div(className='filtros',children=[
        html.H1('Filtros'),    
        html.Div(className='dropdown',children=[
            
                # Dropdowns ocupando 100% da largura da coluna (que já está em 40%)
            dcc.Dropdown(sexo, placeholder='Sexo',id='sexo', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(idade, placeholder='Idade',id='idade', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(nascimento, placeholder='Data de Nascimento',id='nascimento', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(corRaca, placeholder='Cor ou Raça',id='corRaca', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(anoEscolar, placeholder='Ano na Escola',id='anoEscolar', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(pessoasPorCasa, placeholder='Pessoas na casa',id='pessoasPorCasa', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True),
            dcc.Dropdown(esferaAdministrativa, placeholder='Esfera Administrativa',id='esferaAdministrativa', style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},multi=True)
        ]),
        
                    
        html.Div(children=[
            html.H1('Escolha o dado'),
            html.Div(children=[
                dcc.Dropdown(
                    dados, placeholder='Dados', id='selecionarDado', 
                    style={'width': '100%', 'height': '40px', 'font-size': '16px', 'margin-bottom': '10px'},
                    value = dados[0]
                )
            ])
        ]),
                
        html.Div(className='checkbox',children=[
            dcc.RadioItems(
                id='radioItems',
                inline=False,
                value = 'B02019A'
            )      
        ]),
    ]),

    
        # Coluna do Mapa
    html.Div(className= 'mapa',children=[
        html.Iframe(id='map', srcDoc=open('assets/mapabr.html', 'r').read(), width='100%', height='100%')
    ], style={'width': '65%','heigth':'100vh'})  # Ajuste a largura da coluna do mapa para 60%
], style={'display': 'flex'})  # Flex container para organizar as colunas lado a lado

dfPerguntas = pd.read_csv('assets/codigoPerguntas.csv')
#filtro_estado = dfPerguntas[(dfPerguntas['MUNICIPIO_CAP'] == 0)]
dfPerguntas = dfPerguntas[(dfPerguntas['B01001A'] == 9)]
dfPerguntas = dfPerguntas[(dfPerguntas['MUNICIPIO_CAP'] == 0) & (dfPerguntas['UF'] == 41)]
#filtro_estado = filtro_estado[(filtro_estado['UF'] == 11)]

#filtro_estado
dfPerguntas['B02019A']


# %%


@app.callback(
    Output('radioItems', 'options'),
    Input('selecionarDado','value')
)
def radioItems_update(dadoSelecionado):
    if dadoSelecionado == dados[0]:
        return alimentacao_checklist
    if dadoSelecionado == dados[1]:
        return atividade_checklist
    if dadoSelecionado == dados[2]:
        return situacoesCasaEscola_checklist
    if dadoSelecionado == dados[3]:
        return saudeMental_checklist
    if dadoSelecionado == dados[4]:
        return saudeReprodutiva_checklist
    if dadoSelecionado == dados[5]:
        return higiene_checklist
    if dadoSelecionado == dados[6]:
        return usoSaude_checklist
    

# %%


# %%


@app.callback(
    Output('map', 'srcDoc'),
    [Input('radioItems', 'value'),
    Input('sexo', 'value'),
    Input('idade', 'value'),
    Input('nascimento', 'value'),
    Input('corRaca', 'value'),
    Input('anoEscolar', 'value'),
    Input('pessoasPorCasa', 'value'),
    Input('esferaAdministrativa','value')],
    prevent_initial_call=True
)
def mapUpdate(perguntaSelecionada,sexo,idade,nascimento,corRaca,anoEscolar,pessoasPorCasa,esferaAdministrativa):

    Inputs = [sexo,idade,nascimento,corRaca,anoEscolar,pessoasPorCasa,esferaAdministrativa]
    codigos = ['B01001A','B01003','B01005','B01002','B01021A','B01010A','ESFERA']

    if perguntaSelecionada is None:
        return open('mapa.html', 'r').read()
    
    dfPerguntas = pd.read_csv('assets/codigoPerguntas.csv')
    df_filtrado = pd.DataFrame()

    
    taxa = pd.DataFrame({'estados': listSglEstados})
    dadoEstados = pd.DataFrame(columns=['taxa'])

    for i in range(len(Inputs)):
            if Inputs[i] is not None:
                for j in range(len(Inputs[i])):
                    df_filtrado =  pd.concat([df_filtrado,dfPerguntas[dfPerguntas[codigos[i]] == int(Inputs[i][j])]], ignore_index=True)

    print(df_filtrado['ESFERA'])

    for i in UF:
        # Filtrando as linhas para o estado específico e para `MUNICIPIO_CAP == 0`
        filtro_estado = df_filtrado[(df_filtrado['MUNICIPIO_CAP'] == 0) & (df_filtrado['UF'] == i)]
        
        # Calculando a média da coluna representada por `perguntaSelecionada`
        media = filtro_estado[perguntaSelecionada].mean()

        # Adicionando a média calculada no DataFrame `dadoEstados`
        dadoEstados.loc[len(dadoEstados)] = [media]



    
    # Calculando a taxa média para cada capital e adicionando a `dadoEstados`
    for i in codCap:
        # Filtrando as linhas para cada capital específica
        filtro_capital = df_filtrado[df_filtrado['MUNICIPIO_CAP'] == i]
        
        # Calculando a média da coluna representada por `perguntaSelecionada`
        media = filtro_capital[perguntaSelecionada].mean()
        
        # Adicionando a média calculada no DataFrame `dadoEstados`
        dadoEstados.loc[len(dadoEstados)] = [media]



    # Adicionando a coluna 'taxa' ao DataFrame `taxa`
    taxa['taxa'] = dadoEstados['taxa'].values

    taxa.to_csv('taxabr.csv',index=False)
    # Chamando a função para criar o mapa
    CriarMapaFolium.criarMapa('assets/BR2', taxa, perguntasResumidas[perguntaSelecionada])

    # Retornando o conteúdo HTML do mapa gerado
    return open('mapa.html', 'r').read()


# %%
if __name__ == '__main__':
    app.run(debug=True)

# %%



