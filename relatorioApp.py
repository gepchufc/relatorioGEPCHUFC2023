import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# Funções para cada seção e subseção
def apresentacao():
    st.image("Assets/Images/apresetacao-1.png")
    st.markdown("""
    #### REITOR
    Prof. Custódio Luís Silva de Almeida
    
    #### VICE-REITOR 
    Prof. Diana Cristina Silva de Azevedo
                
    #### SUPERINTENDENTE DOS HOSPITAIS UNIVERSITÁRIOS 
    Josenília Maria Alves Gomes 
    
    #### GERENTE DE ENSINO E PESQUISA 
    Renan Magalhães Montenegro Júnior 

    #### CHEFE DO SETOR DE GESTÃO DO ENSINO
    Rômulo Rebouças Lôbo 

    #### CHEFE DO SETOR DE GESTÃO DA PESQUISA E INOVAÇÃO TECNOLÓGICA EM SAÚDE
    Tainá Veras de Sandes Freitas 

    #### CHEFE DA UNIDADE DE APOIO AO ENSINO E PESQUISA 
    Raimundo Homero de Carvalho Neto 

    #### CHEFE DA UNIDADE DE E-SAÚDE 
    Luís Carlos Alexandre Silva

    #### CHEFE DA UNIDADE DE GESTÃO DE GRADUAÇÃO, ENSINO TÉCNICO E EXTENSÃO
    Beatriz Amorim Beltrão 

    #### CHEFE DA UNIDADE DE GESTÃO DE PÓS-GRADUAÇÃO 
    Andréa da Nóbrega Cirino Nogueira Cronemberger

    #### CHEFE DA UNIDADE DE GESTÃO DA PESQUISA
    Érika Gondim Gurgel Ramalho Lima 

    #### CHEFE DA UNIDADE DE GESTÃO DA INOVAÇÃO TECNOLÓGICA EM SAÚDE
    Thisciane Ferreira Pinto Gomes
    """)

def get_image_as_base64(image):
    with open(image, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def gep():
    image_path_renan = "Assets/Images/profRenan.png"
    image_path_organograma = "Assets/Images/organograma2023relgestao.png"

    image_base64 = get_image_as_base64(image_path_renan)
    organograma_base64 = get_image_as_base64(image_path_organograma)

    st.markdown(
        f"""
        <style>
        .centered-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 50%;
            width: 180px;
        }}
        </style>
        <img src="data:image/png;base64,{image_base64}" class="centered-img">
        """,
        unsafe_allow_html=True
    )

    st.header("Gerência de Ensino e Pesquisa")
    st.markdown("""
        Em 2023, a Gerência de Ensino e Pesquisa (GEP) do Complexo Hospitalar da UFC/EBSERH desempenhou um papel crucial na promoção e 
        fortalecimento das atividades de ensino e pesquisa. Localizada estrategicamente no pavimento superior do prédio das Policlínicas 
        Especializadas/Ilhas, a GEP continuou a expandir sua atuação, integrando esforços para manter o CH-UFC/EBSERH como referência em 
        educação e inovação em saúde na região.
    
        Com uma estrutura organizacional enxuta, mas com uma equipe comprometida, a GEP promoveu uma série de iniciativas significativas ao 
        longo do ano. Estas incluíram a expansão de pesquisas clínicas e acadêmicas, destacando-se na rede EBSERH pela condução de inúmeros 
        estudos focados na melhoria dos cuidados de saúde. Além disso, a GEP fortaleceu a integração das atividades educativas com atividades 
        assistências do Complexo, garantindo uma formação prática efetiva e humanizada para o SUS.
    
        O ano também foi marcado por um avanço significativo na utilização de tecnologias no ensino e uso de simulação. O Centro de 
        Simulação/Laboratório de Habilidades teve uma ampliação de seus recursos, com a aquisição de novos equipamentos que enriqueceram o 
        acervo disponível para o treinamento prático e ensino em saúde. Este centro se consolidou como uma ferramenta essencial para a 
        capacitação de residentes e estudantes de graduação, apoiando a realização de procedimentos complexos em um ambiente seguro e controlado.
    
        A infraestrutura e os recursos tecnológicos também foram ampliados com a introdução da impressora 3D e a criação do espaço INOVA-Ensino. Este recurso inovador permitiu a criação de diversos modelos anatômicos, apoiando a pesquisa e o ensino na saúde, além de propiciar avanços significativos no âmbito da inovação.
    
        Por meio destes esforços, a GEP não apenas reforça seu compromisso com a excelência educacional e de pesquisa aplicada, mas também 
        contribui significativamente para a formação de profissionais qualificados, preparados para enfrentar os desafios do cenário de saúde 
        atual e atuação no SUS. A seguir, são descritas no presente documento os principais indicadores e atividades realizadas pela GEP ao 
        longo do ano de 2023.
        """)

    st.markdown(
        f"""
        <style>
        .normal-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
        }}
        </style>
        <img src="data:image/png;base64,{organograma_base64}" class="normal-img">
        <div style="text-align: center;"><em>Organograma da Gerência de Ensino e Pesquisa do CH-UFC/EBSERH (2023).</em></div>
        """,
        unsafe_allow_html=True
    )

def setor_gestao_ensino():
    image_path_romulo = 'Assets/Images/romulo.png'
    image_base64_setor_ensino = get_image_as_base64(image_path_romulo)

    st.markdown(
        f"""
        <style>
        .centered-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 50%;
            width: 180px;
        }}
        </style>
        <img src="data:image/png;base64,{image_base64_setor_ensino}" class="centered-img">
        """,
        unsafe_allow_html=True
    )

    st.header("Setor de Gestão do Ensino")
    st.markdown("""
        Ao longo de 2023, o Setor de Gestão do Ensino e suas unidades vinculadas, em parceria com a Unidade Apoio ao Ensino e Pesquisa, 
        promoveu ações voltadas para integração das atividades didáticas realizadas no CH-UFC/Ebserh com a Faculdade de Medicina, Faculdade 
        de Farmácia, Odontologia e Enfermagem, Conselho do Internato, COREME e COREMU. Para tanto, foram promovidas reuniões sistemáticas com 
        intuito de compartilhar alinhamentos estratégicos e integrar o planejamento das atividades de ensino desenvolvidas no CH-UFC/EBSERH. 
        Em 2023, os Setores atuaram mais marcadamente nas atividades de graduação e pós-graduação realizadas no CH-UFC/EBSERH.
                 
        Desse modo, buscou-se promover maior integração das ações de ensino com as atividades assistenciais realizadas, assegurando, também, 
        a adesão às medidas de segurança ainda requeridas em decorrência da finalização do cenário pandêmico e retorno à normalidade.

        Outrossim, o Setor de Ensino do CH-UFC empreende esforços para ampliar a utilização do Centro de Simulação / Laboratório de Habilidades, 
        sobretudo, por residentes Médicos e Multiprofissionais, incentivando ainda a formação de novos instrutores em Simulação Realística. 

        Em paralelo, houve contribuição direta para a execução do Plano Diretor Estratégico (PDE) 2021-2023 do CH-UFC. Nesse sentido, foram 
        implementadas atividades voltadas para o mapeamento de competências de programas de residência, assim como organização de cursos para 
        capacitação de preceptores. Entre as iniciativas voltadas para o desenvolvimento desses profissionais destacam-se o desenvolvimento de 
        cursos, tanto presenciais como em formato híbrido (presencial e remoto), disponibilizados na plataforma 3EC, como piloto para formação 
        de preceptores e residentes, bem como realização de simulações realísticas. Portanto, as ações realizadas ao longo de 2023 visaram e 
        transfiguraram o alinhamento com a visão do CH-UFC/EBSERH de ser "a melhor sala de aula do norte e nordeste". 

    """)

def unidade_gestao_pos_graduacao():
    st.header("Unidade de Gestão de Pós-Graduação")
    st.markdown("""
        Em 2023, as atividades foram voltadas para os estudantes de Residência Médica e Residência Multiprofissional e em área profissional 
        da saúde. Dessa forma, fluxos e indicadores relativos às atividades supracitadas estão apresentados, em subtópicos, abaixo.
    """)

def atividades_residencia_medica():
    st.header("Atividades de Residência Médica")
    st.markdown("""
        A Residência Médica, instituída pelo Decreto nº 80.281, de 05 de setembro de 1977, pela Lei Federal Nº 6.932, de 07 de julho de 1981, 
        constitui uma modalidade de ensino de pós-graduação destinada a médicos, sob a forma de curso de especialização. As atividades são 
        realizadas em instituições de saúde, sob a orientação de profissionais médicos de elevada qualificação ética e profissional, sendo
        considerada o “padrão ouro” da especialização médica.
        
        A RESOLUÇÃO Nº 01/CEPE, DE 10 DE FEVEREIRO DE 2022 regulamentou, no âmbito da Pró-Reitoria de Pesquisa e Pós-Graduação da Universidade 
        Federal do Ceará, na Seção de Pós-Graduação Lato Sensu, as ações dos programas de Residência Médica, Residências Uniprofissional e 
        Multiprofissional, a saber: 
                
        - Formalização da carga horária docente; 
        - Aproveitamento das disciplinas e cargas horárias dos programas de Residência Médica, Uniprofissional e Multiprofissional, por discentes regularmente matriculados em programas de Pós-Graduação Stricto Sensu da UFC, mediante anuência da coordenação do programa Stricto Sensu; 
        - Disponibilização de módulo próprio, no Sistema Integrado de Gestão de Atividades Acadêmicas, para gestão dos programas de Residência e controle acadêmico dos respectivos discentes.
        
        Os Programas de Residência Médica (PRM) funcionam perante credenciamento oficial pela Comissão Nacional de Residência Médica (CNRM), 
        sob controle administrativo da Pró-Reitoria de Pesquisa e Pós-Graduação da UFC, da Gerência de Ensino e Pesquisa (GEP) do CH-UFC/EBSERH 
        e da Comissão de Residência Médica (COREME) do Complexo Hospitalar da UFC/EBSERH. Os PRM e áreas de atuação credenciados na CNRM estão 
        demonstrados na tabela abaixo.
        
        O aumento da oferta de vagas ao longo dos últimos dez anos (2013-2023), bem como seu respectivo preenchimento a cada ano e o aumento 
        permanente do número de residentes em atividade, demonstra o fortalecimento das atividades da modalidade de pós-graduação em questão no 
        Complexo Hospitalar da UFC, conforme gráfico abaixo.
        """)

    # Carregar os dados do CSV
    df_atividadeDeResMedica = pd.read_csv("Assets/dataSets/Atividade_de_Residencia_Medica.csv")

    # Criar o gráfico interativo
    fig = go.Figure(data=[
        go.Bar(
            x=df_atividadeDeResMedica['Ano'],
            y=df_atividadeDeResMedica['Residentes_Medicos'],
            marker_color='#003F36', 
            marker_line_color='rgb(8,48,107)',
            marker_line_width=1.5,
            opacity=0.6,
            text=df_atividadeDeResMedica['Residentes_Medicos'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        )
    ])

    fig.update_layout(
        title='Número de Residentes Médicos com Atividade no Complexo Hospitalar da UFC/EBSERH (2013-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Residentes',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

    st.markdown("""
        Vale ressaltar a implementação das duas áreas com anos adicionais de atuação: Terceiro ano de residência em clínica médica (medicina 
        interna) e quarto ano em otorrinolaringologia. Ao todo, são 33 programas de Residência médica em 21 áreas de atuação.
    """)

    # Carregar o dataframe de um arquivo csv:
    df_programasResidencia = pd.read_csv("Assets/dataSets/Programas_Residencia_Medica.csv")

    # Filtros interativos
    hospitais = df_programasResidencia['Hospital'].unique()
    hospital_selecionado = st.selectbox("Selecione o hospital:", hospitais, key='hospital1')

    programas = df_programasResidencia['Programa'].unique()
    programas_selecionados = st.multiselect("Selecione os programas:", programas, default=programas, key='programas1')

    # Aplicar os filtros ao DataFrame
    df_filtrado = df_programasResidencia[(df_programasResidencia['Hospital'] == hospital_selecionado) & 
                                         (df_programasResidencia['Programa'].isin(programas_selecionados))]
    
    # Título da tabela
    st.markdown("""###### Programas de residência médica no CH-UFC/Ebserh.""")
    # Exibir o DataFrame formatado de forma interativa
    st.dataframe(df_filtrado)

    # Gráfico referente às áreas de atuação da residência médica
    df_areasAtuacaoResMedica = pd.read_csv("Assets/dataSets/Areas_de_Atuacao.csv")

    # Filtros interativos
    hospitais2 = df_areasAtuacaoResMedica['Hospital'].unique()
    hospital_selecionado2 = st.selectbox("Selecione o hospital:", hospitais2, key='hospital2')

    areasResMedica = df_areasAtuacaoResMedica['Area'].unique()
    areasSelecionadas = st.multiselect("Selecione os programas:", areasResMedica, default=areasResMedica, key='areas1')

    # Aplicar os filtros ao DataFrame
    df_filtrado2 = df_areasAtuacaoResMedica[(df_areasAtuacaoResMedica['Hospital'] == hospital_selecionado2) & 
                                            (df_areasAtuacaoResMedica['Area'].isin(areasSelecionadas))]
    
    # Título da tabela
    st.markdown("""###### Áreas de atuação da residência médica no CH-UFC/Ebserh.""")

    # Exibir o DataFrame formatado de forma interativa
    st.dataframe(df_filtrado2)

def atividades_residencia_multiprofissional():
    st.header("Atividades de Residência Multiprofissional e Uniprofissional da Saúde")
    st.markdown("""
        As Residências Multiprofissionais e Uniprofissionais da Saúde, criadas a partir da promulgação da Lei n° 11.129 de 2005, são orientadas 
        pelos princípios e diretrizes do Sistema Único de Saúde (SUS), a partir das necessidades e realidades locais e regionais, e abrangem as 
        seguintes profissões da área da saúde: Biomedicina, Ciências Biológicas, Educação Física, Enfermagem, Farmácia, Fisioterapia, 
        Fonoaudiologia, Medicina Veterinária, Nutrição, Odontologia, Psicologia, Serviço Social e Terapia Ocupacional 
        (Resolução CNS nº 287/1998). Atualmente, no CH-UFC/EBSERH, estão em atividade três programas, a saber: Residência Integrada 
        Multiprofissional em Atenção Hospitalar à Saúde, Residência em Enfermagem Obstétrica e Residência em Cirurgia e Traumatologia 
        Bucomaxilofacial.
        
        São 3 programas de Residência multiprofissional e uniprofissional não-médicos: RESENFO, RESMULTI E RESBUCO. Foram ofertadas, nesses, 
        61 vagas para residência em 2023 e 58 destas foram ocupadas, resultando em uma taxa de ocupação de 95,1%, conforme ilustrado na figura 
        abaixo. 
        
        As condições da residência estão de acordo com a Lei 6.932 de 07 de julho de 1981, Lei nº 12.514, de 28 de outubro de 2011 (nova redação
        ao art. 4o da Lei no 6.932) e a Portaria Interministerial nº 3, de 16 de março de 2016.
    """)

    # Carregar os dados do CSV
    df_resMulti = pd.read_csv("Assets/dataSets/vagasResMulti.csv")

    # Renomeando colunas
    df_resMulti.columns = ['Ano', 'Oferta de Vagas', 'Matrículas']
    
    # Criar o gráfico interativo
    fig_resMult = go.Figure(data=[
        go.Bar(
            x=df_resMulti['Ano'],
            y=df_resMulti['Oferta de Vagas'],
            name='Oferta de Vagas',
            marker_color='#003F36',
            marker_line_color='rgb(8,48,107)',
            marker_line_width=1.5,
            opacity=0.6,
            text=df_resMulti['Oferta de Vagas'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        ),
        go.Bar(
            x=df_resMulti['Ano'],
            y=df_resMulti['Matrículas'],
            name='Matrículas',
            marker_color='#66C2A5',
            marker_line_color='rgb(8,48,107)',
            marker_line_width=1.5,
            opacity=0.6,
            text=df_resMulti['Matrículas'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        )
    ])

    fig_resMult.update_layout(
        title='Histórico do Quantitativo de Vagas Ofertadas e Matrículas nos Programas de Residência<br> Multiprofissional e Uniprofissional da Saúde (2012-2023)',
        xaxis_title='Ano',
        yaxis_title='Número',
        template='plotly_white',
        barmode='group'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_resMult)

    st.markdown("""
    ##### Cursos ofertados pela Unidade de Gestão da Pós-Graduação em 2023:
                    
    - OFERTA DE VAGAS CURSO BLS E ACLS - iniciativa Hcor em parceria com o Ministério da Saúde - via PROADI/SUS;
    - Curso ACLS - Advanced Cardiologic Life Support (Suporte avançado de Vida em Cardiologia) (duas turmas de 24 residentes médicos e enfermeiros; 21-22/11/2023 e 23-24/11/2023);
    - Curso BLS - Basic Life Support (Suporte Básico de Vida) (uma turma de 30 residentes multiprofissionais e em área profissional da saúde - 21/11/2023);
    - Curso Hospital Amigo da Criança (IHAC);
    - Curso Canguru.

    Produções técnicas, científicas e educativas 

    ##### Artigos publicados em periódicos:

    - Moreira TR, Negreiros FDDS, Aquino MJN, Silva LMSD, Moreira TMM, Torres RAM. Digital technology and its effects on knowledge improvement for diabetes management: An integrative review. Int J Nurs Pract. 2023 Feb;29(1):e13029. doi: 10.1111/ijn.13029. Epub 2021 Dec 11.
    - Magdiel Akbor Alves da Silva, Moreira, T. R., Negreiros, F. D. da S., Araújo, S. T., & Donato, I. M. (2023). Adesão às recomendações de boas práticas em insulinoterapia: relação com o controle glicêmico. Revista De Enfermagem Do Centro-Oeste Mineiro, 13. https://doi.org/10.19175/recom.v13i0.4993
    - Silva DES, Moreira TR, Negreiros FDS, Araújo ST, Silva LMS, Moreira TMM. The effect of nursing consultation on the promotion of safe practices in insulin therapy: a retrospective study. Online Braz J Nurs. 2023;22:e20236601. https://doi.org/10.17665/1676-4285.20236601
    - Dantas NS; Albuquerque NV; Moreira TR; Bezerra AN; Ramos LTT; Rebouças KSC; Mendes RCM. Uso de aplicativos para contagem de carboidratos como ferramenta de auxílio no autogerenciamento do diabetes mellitus tipo 1: uma revisão sistemática. Research, Society and Development, v. 12, n. 1, e3912139270, 2023 (CC BY 4.0) | ISSN 2525-3409 | DOI: http://dx.doi.org/10.33448/rsd-v12i1.39270 .
    - Atuação do farmacêutico residente na equipe multidisciplinar: um relato de experiência do primeiro mês de residência - REVISTA CH-UFC ANO 3 | Nº 4 | SETEMBRO 2023
    - OPTIMIZATION OF THE USE OF BUSULFAN IN THE CONDITIONING OF HEMATOPOIETIC STEM CELL TRANSPLANTATION. Journal of Bone Marrow Transplantation and Cellular Therapy, Vol. 4 No. Suppl1 (2023): Proceedings of XXVII Annual Meeting of the Brazilian Society of Bone Marrow Transplantation and Cellular Therapy

    ##### Artigos publicados em anais de congressos
    - Elaboração de material educativo para pacientes portadores de leucemia mieloide crônica no tratamento com inibidores de tirosina quinase: relato de experiência (VIII Encontro de Iniciação acadêmica)
    - Tecnologias voltadas para a educação em saúde: o que temos para a doença renal crônica? (I Congresso nacional sobre o SUS: desafios e perspectivas)
    - Avaliação da adequação do teor de sódio de uma dieta renal em uma unidade de alimentação e nutrição de um hospital público de Fortaleza (I Congresso Norte Nordeste de Nefrologia)
    - Definição de um bundle de otimização terapêutica como ferramenta de sistematização do cuidado clínico farmacêutico para o manejo dos antimicrobianos (XIV Congresso Brasileiro de Farmácia Hospitalar)
    - Estruturação de guias de segurança de prescrição, preparo e administração de antineoplásicos endovenosos nos serviços de onco-hematologia e transplante de células tronco hematopoiéticas (XIV Congresso Brasileiro de Farmácia Hospitalar)
    - Individualização de dose de medicamento como estratégia de redução de custos: relato de caso (XIV Congresso Brasileiro de Farmácia Hospitalar)
    - Elaboração de instrumentos para melhorar a adesão terapêutica dos pacientes com leucemia mieloide crônica em uso de inibidores da tirosinaquinase (XIV Congresso Brasileiro de Farmácia Hospitalar)

    ##### Desenvolvimento de material educativo:
    - Cartilhas sobre educação para o autocuidado da pessoa com diabetes no contexto hospitalar;
    - Protocolo sobre práticas seguras em insulinoretapia;
    - Cartilha sobre autocuidado no diabetes tipo 1

    ##### Treinamentos:
    - Treinamento sobre práticas seguras em insulinoterapia - 05 e 06/2023. 
    - Treinamento sobre cuidados com os pés e manejo da úlcera do pé diabético - 08/2023;
    - I treinamento de suporte avançado em obstetrícia da MEAC. Curso com oficinas práticas e cenários de simulação (RESMED)
    - Treinamento sobre bomba de insulina
    - Treinamento sobre bomba de insulina - 07/2023
    - I Socorros psicológicos
    - Curso sobre luto
    - Diagnóstico das patologias oncohematológicas no adulto
    - Nutrição em oncologia
    - Farmácia em Onco-hematologia
    - Terapia Celular da Sociedade Brasileira de Terapia Celular e Transplante de Medula Óssea (SBTMO)
    - Curso de aperfeiçoamento de raciocínio clínico no uso de antimicrobianos

    ##### Educação em saúde:
    - Grupos educativos/ Mapas de conversação em DM - Todas às quintas (ambulatório de pediatria) e sextas (ambulatório de endocrinologia);
    - Atividade educativa voltada para pacientes e acompanhantes durante a Semana de Prevenção da Mortalidade Materna - maio 
    - Atividade educativa voltada para pacientes e acompanhantes durante o “Setembro Amarelo”
    - Atividade educativa voltada para os profissionais desta instituição durante o “Outubro Rosa” 
    - Atividade educativa voltada para pacientes e acompanhantes durante a Semana Mundial de Aleitamento Materno - AGOSTO 
    - Atividade educativa voltada para pacientes e acompanhantes durante a Semana da Prematuridade (novembro)
    - Participação em oficinas de simulação realística durante a Semana de Prevenção da Mortalidade Materna
    - Grupo de Terapia Ocupacional em Psicogeriatria (voltado para pacientes do ambulatório de psicogeriatria e do PROAPP, com estimulação cognitiva e socialização); 
    - Grupo de Arteterapia (voltado para pacientes do ambulatório de saúde mental e da enfermaria de saúde mental, com atividades autoexpressivas, artesanais, dentre outras);
    - Grupo de Terapia Comunitária (voltado para pacientes do ambulatório de saúde mental, abordando temas relacionados à saúde mental e demais demandas apresentadas);
    - Ambientoterapia (sala de espera com atividades de respiração, alongamento e psicoeducação);
    - Participação no grupo de artes (GERARTE), voltado para pacientes do ambulatório de psicogeriatria;
    - Grupo de cuidando do cuidador voltado para residentes do Programa RESMULTI com ênfase em Saúde Mental (práticas de relaxamento, meditação guiada, vivências de arteterapia, dentre outras técnicas)
    - Orientação das atividades de residentes no Programa de Apoio ao Paciente Psicótico

    ##### Eventos:
    - Semana do diabetes - 13 a 7/ novembro de 2023;
    - Oficina do Núcleo Docente Assistencial Estruturante;
    - Oficina de elaboração de itens

    ##### Utilização de Simulação Virtual para capacitação de Residentes: 
    - A implementação de capacitação de ventilação mecânica através do uso do Xlung®, plataforma de simulação virtual de alta fidelidade, foi um avanço e tem sido uma ferramenta eficiente no ensino, proporcionando aos profissionais experiências realísticas e ambiente reflexivo para o desenvolvimento de competências essenciais ao cuidado centrado no paciente. 
    - Oficinas de simulação realística durante a Semana de Prevenção da Mortalidade Materna

    ##### Sessões científicas:
    - Sessões multiprofissionais do programa de Residência Integrada Multiprofissional em Atenção Hospitalar à Saúde, área de concentração Oncohematologia (Sessão Blood conteúdo – patologias, protocolos clínicos, tópicos de nutrição e psicologia): 28 SESSÕES
    - Sessões multiprofissionais do Serviço de Oncohematologia (Sessões ofertadas via google Meet às quartas-feiras, para todos os residentes da ResMed e Resmulti da oncohematologia. Conteúdo: doenças oncohematológicas (leucemias e linfomas), protocolos clínicos, temas técnicos promovidos pela indústria farmacêutica): 38 SESSÕES;
    - Sessões clínicas de cada profissão na ênfase (Apresentação de artigos e temas voltados a ênfase. As sessões são conduzidas pelos preceptores. FARMÁCIA: 21; PSICOLOGIA: 11; NUTRIÇÃO: 9; ENFERMAGEM: 14
    - Cine Saúde Mental – exibição de filmes com a temática da saúde mental e discussão posterior, com reflexões sobre os temas abordados
    - Sessão Blood (sessão multiprofissional de residentes da OH): conteúdo – patologias, protocolos clínicos, tópicos de nutrição e psicologia
    - Sessões ofertadas via google meet as quartas-feiras, para todos os residentes da ResMed e Resmulti da oncohematologia. Conteúdo: doenças oncohematológicas (leucemias e linfomas), protocolos clínicos, temas técnicos promovidos pela indústria farmacêutica
    - Sessões clínicas de cada profissão na ênfase Apresentação de artigos e temas voltados a ênfase. As sessões são conduzidas pelos preceptores da Oncohematologia
    - Seminários de saúde mental, o dia da luta antimanicomial, além de ações como o Janeiro Branco e o Setembro Amarelo

    ##### Prática Interdiscilinar
    - Prática interdisciplinar de assistência ao paciente ambulatorial (R1) - terça-feira à tarde - Ambulatório do Adolescente da Maternidade Escola
    - Prática interdisciplinar de assistência ao paciente ambulatorial - Banco de Leite Humano
    - Participação no ambulatório de Psiquiatria Geral (residência multiprofissional  ênfase de saúde mental)
    - Participação em matriciamentos nas Unidades Básicas de Saúde (residência multiprofissional  ênfase de saúde mental)
    - Participação no Ambulatório do Adolescente da MEAC (residência multiprofissional  ênfase SMC)

    ##### Participação em eventos e congressos:
    - I Simpósio em Farmácia Hospitalar e Clínica 
    - XIII Encontro Nacional de Residências em Saúde 
    - VI Encontro de Psicologia 
    - VIII Encontro de Iniciação acadêmica (Farmácia - Elaboração de material educativo para pacientes portadores de leucemia mieloide crônica no tratamento com inibidores de tirosina quinase: relato de experiência)
    - I Simpósio em Farmácia Hospitalar e Farmácia Clínica 
    - I Congresso Norte Nordeste de Nefrologia (Nutrição - Avaliação da adequação do teor de sódio de uma dieta renal em uma unidade de alimentação e nutrição de um hospital público de Fortaleza.) 
    - I Congresso nacional sobre o SUS: desafios e perspectivas (Tecnologias voltadas para a educação em saúde:o que temos para a doença renal crônica?)
    - II Congresso de Ensino, pesquisa e assistência do Complexo Hospitalar da UFC/EBSERH (Nutrição - Proposta de protocolo assistencial de nutrição para pacientes com doença do enxerto contra o hospedeiro de trato gastrintestinal)
    - VI Simpósio Multidisciplinar de Oncohematologia e Imunoterapia 
    - XIV Congresso Brasileiro de Farmácia Hospitalar (“Definição de um bundle de otimização terapêutica como ferramenta de sistematização do cuidado clínico farmacêutico para o manejo dos antimicrobianos”; “Estruturação de guias de segurança de prescrição, preparo e administração de antineoplásicos endovenosos nos serviços de onco-hematologia e transplante de células tronco hematopoiéticas.”; “Individualização de dose de medicamento como estratégia de redução de custos: relato de caso”; “Elaboração de instrumentos para melhorar a adesão terapêutica dos pacientes com leucemia mieloide crônica em uso de inibidores da tirosinaquinase”)
    - XXVII Congresso da Sociedade Brasileira de Terapia Celular e Transplante de Medula Óssea - SBTMO 2023 (Framácia - OPTIMIZATION OF THE USE OF BUSULFAN IN THE CONDITIONING OF HEMATOPOIETIC STEM CELL TRANSPLANTATION. Journal of Bone Marrow Transplantation and Cellular Therapy, Vol. 4 No. Suppl1 (2023): Proceedings of XXVII Annual Meeting of the Brazilian Society of Bone Marrow Transplantation and Cellular Therapy)
    - I Simpósio em Farmácia Hospitalar e Clínica 
    - XIII Encontro Nacional de Residências em Saúde
    - VI Encontro de Psicologia 
    - VIII Encontro de Iniciação acadêmica 
    - I Simpósio em Farmácia Hospitalar e Farmácia Clínica 
    - I Congresso Norte Nordeste de Nefrologia
    - I Congresso nacional sobre o SUS: desafios e perspectivas
    - II Congresso de Ensino, pesquisa e assistência do Complexo Hospitalar da UFC/EBSERH
    - VI Simpósio Multidisciplinar de Oncohematologia e Imunoterapia
    - XIV Congresso Brasileiro de Farmácia Hospitalar
    - IV Encontro de Psicologia do Complexo Hospitalar da UFC/EBSERH

    ##### ATIVIDADES DESENVOLVIDAS PELOS RESIDENTES DE SAÚDE DA MULHER E DA CRIANÇA – 2023
    - No ano de 2023 demos início à prática do Plano Terapêutico Singular (PTS). Nele, os residentes foram distribuídos em três grupos heterogêneos que durante os meses de maio, agosto e novembro de 2023 deveriam rodiziar em três blocos distintos da prática (obstetrícia, ginecologia/mastologia e neonatologia). O projeto oportunizou a discussão de 21 casos clínicos distintos junto às equipes assistenciais
    - Participação em 05 sessões multiprofissionais com todas as residências da MEAC
    - Disciplinas teóricas da área de concentração SMC: Assistência à saúde da criança; Aspectos Psicossociais da Gravidez, Parto e Puerpério; Farmacologia Aplicada à Saúde Materno Infantil; Tópicos Avançados em Saúde da Mulher e da Criança  
    """)

def participacao_plano_diretor():
    st.header("Participação no Plano Diretor Estratégico 2021-2023")
    st.markdown("""
        ---------------------------------------
        ##### Gerente do projeto:
        - Andrea Da Nobrega Cirino Nogueira
        ---------------------------------------
        ##### Problema inicial:
        - Insatisfação dos residentes quanto ao rodízio nos cenários de prática.
        ---------------------------------------
        ##### Solução Proposta:
        - Desenvolver um projeto piloto de capacitação de preceptores sobre avaliação por competências 
            e instituir a figura do coordenador de ensino.
        ---------------------------------------
        ##### Objetivo:
        - Conceber um processo piloto de avaliação por competências nos programas de Residência Médica (Clínica Médica e Ginecologia e 
            Obstetrícia), Uni profissional (Enfermagem Obstétrica e Cirurgia e Traumatologia buco maxilo facial) e Multiprofissional 
            (Diabetes, Oncohematologia, Transplante, Terapia intensiva, Saúde mental e Saúde da mulher e da criança), através de uma 
            capacitação pedagógica que irá desenvolver os futuros orientadores de ensino e, ao mesmo tempo, elaborar as matrizes de 
            competências e processo de avaliação.
        ---------------------------------------
        ##### Benefícios alcançados: 
        - Elaboração/atualização das matrizes de competências dos programas e definição das ferramentas de avaliação;
        - Uma matriz de competências é um instrumento importante para um programa de residência em saúde, pois define as habilidades e 
            conhecimentos necessários para a formação de profissionais qualificados. Ela ajuda a identificar as competências necessárias para 
            cada área de atuação, bem como as estratégias de ensino e avaliação adequadas para cada uma delas.
        - A partir da matriz de competências, é possível planejar o processo de aprendizagem e desenvolvimento dos residentes, proporcionando 
            uma formação mais completa e alinhada com as necessidades do mercado de trabalho. Além disso, permite que o programa de residência 
            seja avaliado e aprimorado continuamente, garantindo a sua eficácia e efetividade.
        - A matriz de competências também é importante para a gestão do programa de residência em saúde, pois auxilia na seleção de candidatos 
            que possuam as habilidades e conhecimentos necessários para cada área de atuação. Ela também ajuda a definir as expectativas dos 
            residentes e a monitorar o seu progresso ao longo do programa. Por fim, a matriz de competências é uma ferramenta que ajuda a 
            padronizar a formação de residentes em saúde, garantindo que todos os profissionais formados pelo programa possuam as competências 
            necessárias para exercer suas funções com qualidade e segurança.
        ---------------------------------------
        ##### Entregas do projeto:
        1. Matrizes de competências dos programas.
        2.	Ferramentas de avaliação.
        3.	Institucionalização do processo avaliativo.
        ---------------------------------------
        ##### Imagens:
        1. Capacitação pedagógica (elaboração das matrizes de competências e ferramentas de avaliação).               
    """)
    st.image("Assets/Images/elabMatrizesCompet.jpg", caption='Equipes trabalhando na elaboração das matriz de competência da residência médica em ginecologia e obstetrícia.')

    st.markdown("""
        2. Exemplos de matrizes de competências elaborados durante o projeto:
    """)
    st.image("Assets/Images/exMatrizCompt.jpg", caption='Matriz de competências da residência médica em clínica médica, segundo a resolução CNRM Nº 14 de 6 de julho de 2021')
    st.image("Assets/Images/exMatrizCompet2.png", caption='Matriz de competência da residência médica em clínica médica do CH-UFC.')
    st.markdown("""
        3. Ferramenta de avaliação:
    """)
    st.image("Assets/Images/ferramentaAvaliacao1.png", caption='Ferramenta de avaliação, MINI CEX, do programa de residência médica em ginecologia e obstetrícia da MEAC.')

def unidade_gestao_graduacao():
    st.header("Unidade de Gestão de Graduação, Ensino Técnico e Extensão")
    st.markdown("""
        Durante o ano de 2023, o Complexo Hospitalar da UFC/Ebserh foi cenário de intensa atividade acadêmica de estudantes de graduação, com a 
        participação de cerca de 1622 estudantes realizando estágios curriculares obrigatórios, aulas práticas e internato na instituição.
    """)

def estagios_obrigatorios_graduacao_multiprofissional():
    st.header("Estágios obrigatórios - Graduação Multiprofissional")
    st.markdown("""
        Cerca de 633 alunos desses alunos são estudantes multiprofissionais vinculados a nove cursos distintos (Enfermagem, Fisioterapia, Farmácia, 
        Nutrição, Educação Física, Pedagogia, Psicologia, Terapia Ocupacional e Serviço Social), refletindo a diversidade e a abrangência do ensino 
        oferecido pela instituição, conforme gráfico representado na figura abaixo. Esta ampla gama de cenários de prática sublinha o compromisso e 
        o potencial do CH-UFC/Ebserh para contribuir na formação prática abrangente e interdisciplinar, preparando os alunos para enfrentar os 
        desafios multifacetados do cenário de saúde atual.
    """)

    # Carregar os dados do CSV
    df_Est_mult = pd.read_csv("Assets/dataSets/Estagios_Obrigatorios_Graduacao_Multiprofissional.csv')

    # Criar o gráfico interativo
    fig_est_mult = go.Figure(data=[
        go.Bar(
            x=df_Est_mult['Curso'],
            y=df_Est_mult['Quantidade'],
            marker_color='#003F36',  
            text=df_Est_mult['Quantidade'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        )
    ])

    fig_est_mult.update_layout(
        title='Quantitativo de estudantes multiprofissionais com atividade no CH-UFC/EBSERH de acordo com o<br> curso de graduação (2023)',
        xaxis_title='Curso',
        yaxis_title='Quantidade',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_est_mult)

    st.markdown("""
        Esses alunos de categorias multiprofissionais que realizaram atividades práticas no CH-UFC/Ebserh em 2023 eram provenientes exclusivamente 
        de instituições públicas de ensino superior, evidenciando uma colaboração estreita e produtiva com a Universidade Federal do Ceará (UFC), a 
        Universidade Estadual do Ceará (UECE) e a Universidade da Integração Internacional da Lusofonia Afro-Brasileira (UNILAB), conforme gráfico 
        representado pela figura abaixo. Esta restrição segue as diretrizes anteriormente estabelecidas pela sede da Ebserh, de modo que mantivemos 
        em 2023 a recomendação de suspender a formalização de convênios com Instituições de Ensino Superior privadas para utilização do HUWC e MEAC 
        como campos de prática.
    """)

    # Carregar os dados do CSV
    df_estudantes = pd.read_csv("Assets/dataSets/Estudantes_Multiprofissionais_IES.csv')

    # Criar o gráfico interativo
    fig_est_mult_IES = go.Figure()

    fig_est_mult_IES.add_trace(go.Bar(
        y=df_estudantes['Ano'],
        x=df_estudantes['UFC'],
        name='UFC',
        orientation='h',
        marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),
        text=df_estudantes['UFC'], textposition='inside'
    ))

    fig_est_mult_IES.add_trace(go.Bar(
        y=df_estudantes['Ano'],
        x=df_estudantes['UNILAB'],
        name='UNILAB',
        orientation='h',
        marker=dict(color='#008D79', line=dict(color='#008D79', width=2)),
        text=df_estudantes['UNILAB'], textposition='inside'
    ))

    fig_est_mult_IES.add_trace(go.Bar(
        y=df_estudantes['Ano'],
        x=df_estudantes['UECE'],
        name='UECE',
        orientation='h',
        marker=dict(color='#02EBC9', line=dict(color='#02EBC9', width=2)),
        text=df_estudantes['UECE'], textposition='inside'
    ))

    fig_est_mult_IES.add_trace(go.Bar(
        y=df_estudantes['Ano'],
        x=df_estudantes['IES PRIVADAS'],
        name='IES PRIVADAS',
        orientation='h',
        marker=dict(color='#78F4E2', line=dict(color='#78F4E2', width=2)),
        text=df_estudantes['IES PRIVADAS'], textposition='inside'
    ))

    fig_est_mult_IES.update_layout(
        barmode='stack',
        title='Quantitativo de estudantes multiprofissionais com atividades no CH-UFC/EBSERH de acordo com a<br> IES (2020-2023)',
        xaxis_title='Número de Estudantes',
        yaxis_title='Ano',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_est_mult_IES)

    st.markdown("""
        Para viabilizar as atividades de ensino de graduação no CH-UFC/Ebserh, ao longo do ano, a UGETE acolheu e manteve interlocução direta 
        com aproximadamente 70 docentes dessas IES. A unidade gerenciou proativamente as solicitações de estágio e aulas práticas encaminhadas 
        pelos professores, além de cuidar da recepção, processamento e arquivamento da documentação necessária para a formalização e adequada 
        execução dessas atividades de ensino.
                
        Em relação à distribuição dos estudantes entre os Hospitais Universitários da UFC, 447 estudantes multiprofissionais participaram de 
        atividades práticas no Hospital Universitário Walter Cantídio (HUWC), enquanto 320 utilizaram as instalações da Maternidade Escola 
        Assis Chateaubriand (MEAC) para esse fim. É importante destacar que alguns alunos participaram de atividades em mais de uma disciplina, 
        o que envolveu a realização de práticas em ambos os hospitais. Dos 633 alunos multiprofissionais que tiveram o CH-UFC/EBSERH como campo 
        de prática, 70,3% eram provenientes da UFC, 22,7% da UNILAB, e 7,0% da UECE. 
    """)

    # Gráfico Distribuição de estudantes multiprofissionais com atividades de graduação no HUWC e MEAC por Instituição de Ensino Superior de origem (2023).
    df_novo_grafico = pd.read_csv("Assets/dataSets/Estudantes_Multiprofissionais_HUWC_MEAC.csv")

    fig_novo_grafico = go.Figure(data=[
        go.Bar(
            y=df_novo_grafico['Instituicao'],
            x=df_novo_grafico['HUWC'],
            name='HUWC',
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),
            text=df_novo_grafico['HUWC'], textposition='inside'
        ),
        go.Bar(
            y=df_novo_grafico['Instituicao'],
            x=df_novo_grafico['MEAC'],
            name='MEAC',
            orientation='h',
            marker=dict(color='#008D79', line=dict(color='#008D79', width=2)),
            text=df_novo_grafico['MEAC'], textposition='inside'
        )
    ])

    fig_novo_grafico.update_layout(
        barmode='stack',
        title='Distribuição de estudantes multiprofissionais com atividades de graduação no HUWC e MEAC<br> por Instituição de Ensino Superior de origem (2023)',
        xaxis_title='Número de Estudantes',
        yaxis_title='Instituição',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_novo_grafico)

    # Número de estudantes multiprofissionais com atividades de graduação no HUWC e MEAC por curso (2023).
    df_est_mult_HUWC_MEAC_Cursos = pd.read_csv("Assets/dataSets/Estudantes_Multiprofissionais_HUWC_MEAC_Cursos.csv")

    fig_est_mult_HUWC_MEAC_Cursos = go.Figure(data=[
        go.Bar(
            y=df_est_mult_HUWC_MEAC_Cursos['Curso'],
            x=df_est_mult_HUWC_MEAC_Cursos['HUWC'],
            name='HUWC',
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),
            text=df_est_mult_HUWC_MEAC_Cursos['HUWC'], textposition='inside'
        ),
        go.Bar(
            y=df_est_mult_HUWC_MEAC_Cursos['Curso'],
            x=df_est_mult_HUWC_MEAC_Cursos['MEAC'],
            name='MEAC',
            orientation='h',
            marker=dict(color='#008D79', line=dict(color='#008D79', width=2)),
            text=df_est_mult_HUWC_MEAC_Cursos['MEAC'], textposition='inside'
        )
    ])

    fig_est_mult_HUWC_MEAC_Cursos.update_layout(
        barmode='stack',
        title='Número de estudantes multiprofissionais com atividades de graduação no HUWC e MEAC<br> por curso (2023)',
        xaxis_title='Número de Estudantes',
        yaxis_title='Curso',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_est_mult_HUWC_MEAC_Cursos)

def estagios_obrigatorios_graduacao_medica():
    st.header("Estágios obrigatórios - Graduação Médica")
    st.markdown("""
        O Complexo recebeu cerca de 989 alunos de graduação de medicina para atividades na instituição. Desses, 480 eram alunos da FAMED-UFC 
        que utilizaram o HUWC e a MEAC para realização de aulas práticas em áreas específicas correspondentes às disciplinas curriculares da 
        formação médica. Além desses, o Complexo foi campo de prática de 509 estudantes do internato médico, sendo 343 alunos vinculados à UFC 
        e 166 pertencentes à outras IES. 
    
        Oito grandes áreas do CH-UFC/EBSERH recebem esses internos de Medicina para realização de suas atividades curriculares, sendo elas: 
        Clínica Médica, Ginecologia e Obstetrícia, Pediatria, Cirurgia, Saúde Mental, Neonatologia, Saúde Comunitária e Saúde Coletiva (ver 
        figura abaixo). Vale salientar que, dentro da área de Clínica Médica, os estudantes rodiziam ainda entre os serviços de 
        Gastroenterologia, Cardiologia, Hematologia, Psiquiatria, Endocrinologia, Nefrologia, Reumatologia, Neurologia, Dermatologia, 
        Pneumologia, Unidade de Terapia Intensiva e Geriatria.
    """)

    # Carregar os dados do CSV
    df_estagios_medica = pd.read_csv("Assets/dataSets/Estagios_Obrigatorios_Graduacao_Medica.csv")

    # Criar o gráfico interativo
    fig_estagios_medica = go.Figure(data=[
        go.Bar(
            y=df_estagios_medica['Area_de_Atuacao'],
            x=df_estagios_medica['Rodizio_UFC'],
            name='Rodízio UFC',
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),
            text=df_estagios_medica['Rodizio_UFC'], textposition='inside'
        ),
        go.Bar(
            y=df_estagios_medica['Area_de_Atuacao'],
            x=df_estagios_medica['Eletivo_HUWC'],
            name='Eletivo HUWC',
            orientation='h',
            marker=dict(color='#008D79', line=dict(color='#008D79', width=2)),
            text=df_estagios_medica['Eletivo_HUWC'], textposition='inside'
        ),
        go.Bar(
            y=df_estagios_medica['Area_de_Atuacao'],
            x=df_estagios_medica['Eletivo_MEAC'],
            name='Eletivo MEAC',
            orientation='h',
            marker=dict(color='#02EBC9', line=dict(color='#02EBC9', width=2)),
            text=df_estagios_medica['Eletivo_MEAC'], textposition='inside'
        )
    ])

    fig_estagios_medica.update_layout(
        barmode='stack',
        title='Quantitativo de estudantes do internato em Medicina com atividades no CH-UFC/EBSERH<br>de acordo com as grandes áreas de atuação (2023)',
        xaxis_title='Número de Estudantes',
        yaxis_title='Área de Atuação',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_estagios_medica)

    st.markdown("""
        No ano de 2023, aproximadamente 267 alunos do internato médico da UFC cumpriram na instituição quase a totalidade dos rodízios dos dois 
        últimos anos de sua formação. Ademais, outros de 242 alunos pertencentes à UFC ou a outras IES realizaram no HUWC ou na MEAC o rodízio 
        eletivo do internato Médico.
                
        Em relação à IES de origem dos estudantes, mais de 67% dos internos de medicina com atividades no Complexo pertenciam à UFC, seguidos 
        por 26% dos alunos oriundos de outras IES públicas e 6% vinculados a instituições particulares de ensino (ver figura abaixo).

    """)

    # Carregar os dados do CSV
    df_internato_ies_origem = pd.read_csv("Assets/dataSets/Internato_Medico_IES_Origem.csv")

    # Criar o gráfico interativo
    fig_internato_ies_origem = go.Figure(data=[
        go.Bar(
            y=df_internato_ies_origem['Instituicao'],
            x=df_internato_ies_origem['Quantidade'],
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),
            text=df_internato_ies_origem['Quantidade'], textposition='inside'
        )
    ])

    fig_internato_ies_origem.update_layout(
        title='Quantitativo de estudantes do internato em Medicina com atividades no CH-UFC/EBSERH<br>de acordo com a Instituição de Ensino Superior de Origem (2023)',
        xaxis_title='Número de Estudantes',
        yaxis_title='Instituição de Ensino Superior',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_internato_ies_origem)

def controle_regulacao_estagios():
    st.header("Controle e regulação de estágios de graduação")
    st.markdown("""
        Considerando que os alunos podem necessitar de cumprir estágios em múltiplas disciplinas ao longo do ano, com planos de atividades 
        distintos para cada uma, é essencial que cada disciplina formalize um Termo de Compromisso de Estágio (TCE) ou um Formulário de Prática 
        Assistida (FPA) com a instituição. No momento da assinatura desses documentos, a UGETE verifica a vigência da apólice de seguro 
        obrigatório, contratada pelas IES a favor do estudante, e assegura-se o cumprimento dos limites de carga horária diária e semanal 
        estipulados por lei. Adicionalmente, realiza-se o cadastro do aluno em uma planilha de acompanhamento de estágio, facilitando o acesso 
        e o monitoramento das atividades autorizadas pela UGETE através do Painel de Estágio Obrigatório do CH-UFC/EBSERH. Este painel está 
        disponível online por meio da Ferramenta FAPIS, o que reforça o controle e a transparência dessas atividades.
        
        Além dos procedimentos documentais descritos, para os alunos em internato são também confeccionados crachás institucionais, realizados 
        registros nos sistemas internos (AGHU, MASTER, SGPTI e FICAR) e promovida oficina de acolhimento presencial para transmitir normas, 
        rotinas e informações cruciais, garantindo uma integração efetiva dos novos internos.
    """)

def estagios_nao_obrigatorios():
    st.header("Estágios não obrigatório")
    st.markdown("""
        Em relação aos Estágios Não-Obrigatórios, ao longo do ano de 2023, cerca de 97 estudantes de dois cursos de graduação distintos 
        participaram de atividades práticas complementares à sua formação acadêmica no Complexo. Destes, 75 eram alunos de Medicina e 22 de 
        Farmácia (ver gráfico, representado pela imagem abaixo).
    """)

        # Carregar os dados do CSV
    df_estagios_nao_obrigatorios = pd.read_csv("Assets/dataSets/Estagios_Nao_Obrigatorios.csv")

    # Criar o gráfico interativo
    fig_estagios_nao_obrigatorios = go.Figure(data=[
        go.Bar(
            x=df_estagios_nao_obrigatorios['Curso'],
            y=df_estagios_nao_obrigatorios['Quantidade'],
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),  
            text=df_estagios_nao_obrigatorios['Quantidade'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        )
    ])

    fig_estagios_nao_obrigatorios.update_layout(
        title='Distribuição dos de estágio não-obrigatório no Complexo de acordo com o curso de<br> graduação (2023)',
        xaxis_title='Curso',
        yaxis_title='Quantidade',
        template='plotly_white'
    )

    fig_estagios_nao_obrigatorios.update_yaxes(range=[0, 80])

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_estagios_nao_obrigatorios)
    
    st.markdown("""
        As atividades foram predominantemente realizadas no Hospital Universitário Walter Cantídio que receberam 90 estudantes, enquanto 7 
        estudantes realizaram suas práticas de estágio não obrigatório na Maternidade Escola Assis Chateaubriand. Os principais cenários dessas 
        práticas incluíram as áreas cirúrgicas, o Laboratório de Análises Clínicas e a Unidade de Terapia Intensiva Clínica do HUWC (ver 
        Gráfico representado pela imagem abaixo).
    """)

    # Carregar os dados do novo CSV para a segunda imagem
    df_estagios_nao_obrigatorios_setor = pd.read_csv("Assets/dataSets/Estagios_Nao_Obrigatorios_Setor.csv")

    # Criar o gráfico interativo
    fig_estagios_nao_obrigatorios_setor = go.Figure(data=[
        go.Bar(
            x=df_estagios_nao_obrigatorios_setor['Quantidade'],
            y=df_estagios_nao_obrigatorios_setor['Unidade_Sector'],
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=2)),  
            text=df_estagios_nao_obrigatorios_setor['Quantidade'],  # Adiciona os valores aos dados
            textposition='outside',  # Define a posição dos textos
        )
    ])

    fig_estagios_nao_obrigatorios_setor.update_layout(
        title='Número de estudantes em estágio não-obrigatório com atividades no CH-UFC/EBSERH<br>de acordo com unidade/setor de atividade (2023)',
        xaxis_title='Quantidade',
        yaxis_title='Unidade/Sector de Atividade',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_estagios_nao_obrigatorios_setor)

    st.markdown("""
        Esses estágios proporcionaram aos alunos a oportunidade de aplicar conhecimentos teóricos em contextos práticos reais, reforçando o 
        aprendizado e preparando-os para desafios futuros em suas carreiras profissionais. A interação direta com pacientes e a participação
        em procedimentos complexos oferecem uma experiência complementar ao aluno em formação, promovendo o desenvolvimento de competências 
        essenciais na área de saúde. 
        
        A UGETE emprega esforços para gerenciar as atividades de estágios curriculares não-obrigatórios no CH-UFC, garantindo que as 
        solicitações sejam devidamente pactuadas e aprovadas pelos docentes orientadores, supervisores de campo e chefias dos serviços 
        envolvidos. Além disso, a unidade zela para que todos os estudantes formalizem o Termo de Compromisso de Estágio e submetam relatórios 
        parciais e finais das atividades realizadas, emitindo ainda o certificado de conclusão do estágio não obrigatório. Esses esforços são 
        direcionados para promover as melhores práticas educacionais e assegurar a conformidade com a Lei 11.788/2008 e outros regulamentos 
        que orientam a realização de estágios não-obrigatórios na UFC, fortalecendo assim a legitimidade, integridade e a qualidade do processo
        formativo.
    """)

def ensino_simulacao():
    st.header("Ensino baseado em Simulação")
    st.markdown("""
        O Complexo Hospitalar da UFC/EBSERH dispõe de um Centro de Simulação / Laboratório de Habilidades localizado na Unidade de Pesquisa 
        Clínica da Gerência de Ensino e Pesquisa. O Centro, operado sob a coordenação do Setor de Gestão do Ensino e UGETE, está equipado e 
        funcionante. A estrutura flexível do centro dispõe de três salas que permitem a reprodução de diferentes ambientes hospitalares e 
        ambulatoriais, como consultórios, leitos de internação, unidades de emergência, terapia intensiva e centro obstétrico. Além disso, 
        conta ainda com outras duas salas dedicadas à observação e centro de controle dos manequins, e um laboratório específico para o 
        treinamento de habilidades cirúrgicas.
        
        Durante o ano de 2023, foram realizados esforços para otimizar o uso da simulação realística na educação e treinamento de estudantes e 
        profissionais do Complexo, especialmente nos programas de residência. Paralelamente, o Setor de Ensino e a UGETE planejaram a aquisição 
        de novos equipamentos e materiais para expandir o acervo de simulação, melhorando assim a capacidade de treinamento prático no CH-UFC.
    """)

    st.image("Assets/Images/simulacao1.jpg", caption='Leito de UTI do Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH (2023).')

    st.image("Assets/Images/simulacao2.jpg", caption='Leito de Unidade Neonatal do Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH (2023).')

    st.image("Assets/Images/simulacao3.jpg", caption='Leito de enfermaria do Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH (2023).')

    st.markdown("""
        Equipado com simuladores de alta, média e baixa fidelidade, o Centro de Simulação tem possibilitado a realização de diferentes tipos de 
        treinamentos nas áreas de Saúde do Adulto, Saúde da Mulher e da Criança, Cirurgia e diversas outras especialidades. 

        Em 2023, foram realizados treinamentos multiprofissionais em reanimação e parada cardiorrespiratória por simulação. No mesmo ano 
        concluiu-se os ciclos de capacitação em primeiros socorros, destinados a terceirizados e assistentes administrativos do CH-UFC, sendo 
        treinados 163 colaboradores. Manequins do centro de simulação também foram utilizados para diversos treinamento de residentes médicos e 
        multiprofissionais. 
    """)

    st.image("Assets/Images/simulacao4.jpg", caption='Curso de primeiros socorros para terceirizados e assistentes administrativos do CH-UFC/Ebserh. Fortaleza, 2023.')

    st.markdown("""
        Um curso de atualização em debriefing na modalidade in company foi oferecido a preceptores e docentes do Complexo, com o objetivo de 
        desenvolver competências para a realização de debriefings significativos. A capacitação ofertada propiciou uma discussão aprofundada 
        acerca das diversas técnicas e estilos, adaptados às variadas necessidades do momento de debriefing.
    """)

    st.image("Assets/Images/simulacao5.jpg", caption='Curso de atualização em debriefing. Fortaleza, 2023.')

def acervo():
    st.header("Acervo")
    st.markdown("""
        Atualmente, o acervo é composto por quatro manequins de alta fidelidade, sendo um adulto, uma gestante e dois neonatos. Os manequins 
        respondem fisiologicamente às mais diversas e adversas situações clínicas, sendo utilizados para elaboração de cenários simulando 
        atendimento de pacientes em situações diversas.

        Além desses, foram adquiridos em 2023 outros dois manequins de média fidelidade em versão adulto, para viabilizar o treinamento em 
        suporte avançado de vida cardiovascular. Esses modelos somam-se ao acervo preexistente de outros manequins de média fidelidade em suas 
        versões adulta e neonatal (bebês a termo e prematuros), além de pelves e acessórios para treinamentos diversos na área de Ginecologia e 
        obstetrícia (figura abaixo ). Com maior possibilidade de deslocamento, esses são frequentemente empregados para realização de 
        atividades in situ com colaboradores. Assim, tais simuladores têm tido fundamental importância no sentido de conferir maior realidade 
        às capacitações estruturadas para implementação e/ou adequação de rotinas e fluxos institucionais, bem como treinamento voltados à 
        realização de vários procedimentos técnicos, como parada cardiorrespiratória, intubação orotraqueal , sondagens, aspirações e punções 
        venosas.
    """)

    st.image("Assets/Images/acervo1.jpg", caption='Torsos para treinamento de reanimação cardiorespiratória em suas versões neonatal, infantil e adulto disponíveis no Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH.')

    st.markdown("""
        Com maior possibilidade de deslocamento, esses são frequentemente empregados para realização de atividades in situ com colaboradores. 
        Assim, tais simuladores têm tido fundamental importância no sentido de conferir maior realidade às capacitações estruturadas para 
        implementação e/ou adequação de rotinas e fluxos institucionais, bem como treinamento voltados à realização de vários procedimentos 
        técnicos, como parada cardiorrespiratória, intubação orotraqueal, sondagens, aspirações e punções venosas.  

        Modelos de baixa fidelidade também estão disponíveis no Laboratório de Habilidades para utilização em treinamentos de técnicas e 
        procedimentos mais fundamentais. Em 2023 foram recebidos da Ebserh sede 21 torsos entre suas versões adulto, infantil e neonatal. 
        Essa ampliação e diversificação do acervo visa a ampliar as possibilidades de treinamentos de técnicas de reanimação cardiopulmonar e 
        suporte básico de vida entre residentes, estudantes e profissionais do Complexo. 

        Além desses, outros manequins de baixa fidelidade, que utilizam materiais como silicone e EVA para reprodução de estruturas humanas, 
        também compõem o acervo e são utilizados para o aprimoramento de diversas técnicas intervencionistas e procedimentos adotados em 
        cirurgias abertas. Residentes de cirurgia geral e, sobretudo, alunos do internato em Medicina da UFC, utilizam esses modelos para 
        treinamentos específicos. 

        Por fim, cinco simuladores de caixas de videolaparoscopia estão também disponíveis e tem papel fundamental no desenvolvimento de 
        habilidades mais avançadas (figura abaixo ). Estes tem possibilitado o treinamento de residentes em procedimentos como realização de 
        suturas em videocirurgia.
    """)

    st.image("Assets/Images/acervo2.jpg", caption='Caixas para simulação de cirurgias videolaparoscópicas no Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH.')

    st.image("Assets/Images/acervo3.jpg", caption='Residentes utilizando simuladores para treinamento de cirurgias videolaparoscópica no Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH.')

    st.image("Assets/Images/acervo4.jpg", caption='Simulação de alta fidelidade com residentes e preceptores no Centro de Simulação / Laboratório de Habilidades do CH-UFC/EBSERH.')

def inovacao():
    st.header("Inovação")
    st.markdown("""
        Em 2023 a GEP adquiriu a primeira impressora 3D do CH-UFC/Ebserh. O modelo Ender 3 S1 da Creality 3D oferece potenciais avanços nas 
        práticas de ensino, pesquisa e inovação no âmbito do CH-UFC/Ebserh. Este equipamento foi alocado no recém-estabelecido espaço da GEP 
        denominado INOVA-Ensino, e tem funcionado em parceria com o Centro de Simulação e a Unidade de Gestão da Inovação Tecnológica em Saúde. O investimento realizado reforça o compromisso com a qualidade e vanguarda na formação acadêmica e técnica dos estudantes e profissionais vinculados ao CH-UFC/Ebserh. 

        O equipamento permite a impressão 3D por meio da técnica de adição sequencial de material, camada por camada, transformando arquivos 
        digitais em objetos sólidos tridimensionais. Este método destaca-se por sua capacidade de produzir estruturas detalhadas com eficiência 
        otimizada em relação aos métodos convencionais de produção, tendo ainda como vantagem a economicidade envolvida na fabricação.

        No contexto educacional, a aplicação da impressão 3D oferece potencial para ampliar o escopo da simulação em treinamentos de 
        procedimentos complexos, aprimorando tanto o desenvolvimento de habilidades procedurais fundamentais, como também o treinamento mais 
        complexo de especialistas. Desse modo pode contribuir para práticas assistenciais mais seguras para os pacientes. 

        Para a área de simulação em saúde, isto implica na capacidade de desenvolver estruturas e modelos anatômicos realísticos para formação e 
        capacitação especializada de profissionais da saúde. Por meio das peças produzidas estudantes, residentes profissionais e docentes do 
        CH-UFC podem expandir as oportunidades de treinamento simulado e aprimoramento de diversas habilidades práticas específicas.

        Com a chegada do equipamento, em 2023 cinco iniciativas piloto foram iniciadas e o êxito nas etapas preliminares de produção já refletem 
        a vasta gama de aplicações e potencial desta tecnologia. Estão em fase final de validação peças que simulam o osso temporal e mastoide 
        para treinamento de cirurgias otológicas, um esterno para treinamento da técnica de punção aspirativa de medula óssea, uma articulação 
        de joelho para treinamento de artrocentese com potencial para possibilitar a prática de artroscopia na região, uma caixa torácica com 
        estruturas internas que permitem o treinamento da técnica de drenagem torácica em pacientes neonatais e uma pelve que possibilita a 
        prática de procedimentos como cerclagem e bloqueio de nervo pudendo. 
    """)

    st.image("Assets/Images/inovacao1.jpg", caption='Modelo de tórax neonatal desenvolvido localmente por meio de impressão 3d e moulage para treinamento das técnicas de drenagem torácia neonatal (2023).')

    st.markdown("""
        As peças inovadoras desenvolvidas no Centro irão integrar o acervo, propiciando realismo e diversificação aos treinamentos envolvendo 
        simulação, sobretudo em áreas em que a prática desses procedimentos é rara ou põe em risco a segurança dos pacientes. Além disso, 
        parte desses produtos tem características inovadoras e grande potencial para serem registrados como novas patentes.   

        Além disso, o software que acompanha os manequins de alta fidelidade utilizado para controle dos mesmos passou por novos aprimoramentos, 
        ganhando personalizações exclusivas do Centro. Foram desenvolvidas localmente telas adicionais e exclusivas do CH-UFC/EBSERH que são 
        exibidas para representar com maior realismo diversos resultados de exames como glicemia e exames laboratoriais ou reprodução animada de 
        aspectos dinâmicos do cenário, tais como progressão da diurese do paciente simulado em atendimento acompanhada também da reprodução de 
        seu aspecto visual. 

        Essas inovações agregadas ao software de controle do manequim possibilitam aos participantes da simulação observarem, de forma ainda mais 
        realística, as respostas das intervenções realizadas durante o curso do cenário simulado. Algumas dessas respostas muitas vezes não são 
        passíveis de serem observadas de forma célere (tal como a diurese do manequim) sem que haja uma interrupção da simulação em andamento. 

        Assim, as inovações produzidas possibilitam exibir resultados e informações relevantes ao cenário com muito mais agilidade e em layout 
        amigável para os participantes e controlador. Por meio dessas novas telas desenvolvidas localmente, a realização dos cenários de alta 
        fidelidade tornou-se ainda mais fidedigna, dinâmica e interativa.
    """)

def centro_simulacao():
    st.header("Utilização do centro de simulação")
    st.markdown("""
        Em 2023, o Centro de Simulação/Laboratório de Habilidades do CH-UFC/EBSERH continuou a ser um recurso importante para o aprimoramento de 
        conhecimentos, habilidades e atitudes, sobretudo entre residentes e alunos de graduação, demonstrando uma utilização efetiva e crescente 
        ao longo dos anos. A quantidade de participantes nas simulações aumentou ligeiramente em relação ao ano anterior, refletindo o compromisso 
        contínuo da instituição com a educação e a formação de qualidade.
    """)

    # Carregar os dados do CSV
    df_simulacao = pd.read_csv("Assets/dataSets/centro_simulacao.csv')

    # Criar o gráfico interativo
    fig_simulacao = go.Figure(data=go.Scatter(
        x=df_simulacao['Ano'],
        y=df_simulacao['Participantes'],
        mode='lines+markers+text',
        line=dict(color='#003F36', width=2),
        marker=dict(size=8, color='#003F36', line=dict(width=2, color='white')),
        text=df_simulacao['Participantes'],
        textposition='top center'
    ))

    fig_simulacao.update_layout(
        title='Demonstrativo do quantitativo de participantes de atividades simuladas realizadas no Centro de<br> Simulação/Laboratório de Habilidades do CH-UFC/EBSERH<br>(2020-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Participantes',
        yaxis=dict(range=[0, 1500]),  
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_simulacao)

    st.markdown("""
        Durante o ano, o Centro contou com cerca de 1053 participações nas diversas simulações realizadas. O aumento representativo de cenários e 
        uso do Centro reflete a integração da simulação na formação de estudantes e profissionais do Complexo.
    """)

      # Carregar os dados do CSV
    df_simulacao = pd.read_csv("Assets/dataSets/centro_simulacao_categoria.csv")

    # Criar o gráfico interativo
    fig_simulacao = go.Figure()

    categorias = df_simulacao['Categoria'].unique()
    anos = df_simulacao['Ano'].unique()

    colors = {'Residentes': '#003F36', 'Alunos de Graduação': '#008D79'}

    for categoria in categorias:
        df_categoria = df_simulacao[df_simulacao['Categoria'] == categoria]
        fig_simulacao.add_trace(go.Bar(
            x=df_categoria['Ano'],
            y=df_categoria['Participantes'],
            name=categoria,
            marker_color=colors[categoria],
            text=df_categoria['Participantes'],
            textposition='outside'
        ))

    fig_simulacao.update_layout(
        barmode='group',
        title='Quantitativo de residentes e graduandos participantes de atividades simuladas realizadas no<br> Centro de Simulação/Laboratório de Habilidades do CH-UFC/EBSERH<br>por categoria (2020-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Participantes',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_simulacao)

    st.markdown("""
        Foram realizadas ao longo de 2023 simulações em áreas como Pediatria, Cirurgia, Semiologia, Pneumologia, Clínica Médica, Terapia Intensiva, 
        e Ginecologia e Obstetrícia, com um total de 178 cenários executados. Essas atividades permitiram aos participantes vivenciarem de modo 
        realístico situações clínicas complexas e a desenvolver habilidades essenciais em um ambiente controlado e seguro.
    """)


def unidade_apoio_ensino_pesquisa():
    st.header("Unidade de Apoio ao Ensino e à Pesquisa")
    st.markdown("""
        O principal destaque da Unidade de Apoio ao Ensino e à Pesquisa do Complexo Hospitalar da Universidade Federal do Ceará neste período 
        foi a realização do I Curso de Suporte Avançado em Obstetrícia da MEAC, ocorrido de 25 a 27 de outubro de 2023. Este curso inovador 
        foi desenhado para oferecer treinamento de ponta a uma ampla gama de profissionais da saúde, com foco no manejo seguro e eficiente de 
        diversas situações obstétricas críticas.

        Ao longo de três dias, o curso abordou temas cruciais como o Manejo Seguro do Parto Pélvico, Reanimação Neonatal, Distocia de Ombro, 
        Comunicação de Más Notícias, Diagnóstico e Abordagem das Pacientes com Sepse, entre outros, através de uma metodologia que combinou 
        estações práticas com simulação realística, aulas expositivas e discussões de casos clínicos. Facilitadores altamente qualificados e 
        experientes lideraram cada sessão, assegurando que os participantes adquirissem conhecimentos práticos e teóricos fundamentais para a 
        prática obstétrica.

        A diversidade dos profissionais inscritos evidencia o reconhecimento e a necessidade do curso no ambiente hospitalar e na formação 
        continuada das equipes de saúde. Com 118 residentes de medicina, 23 médicos, 39 enfermeiros, 2 internos, 1 dentista, 1 psicóloga, 30 
        auxiliares e técnicos de enfermagem, 3 acadêmicos de enfermagem, 11 residentes multidisciplinares, 9 residentes de enfermagem e 1 
        residente externo especial, o curso alcançou uma ampla gama de profissionais interessados em aprimorar suas habilidades em obstetrícia.

        Este curso representa um marco na busca contínua da excelência no cuidado obstétrico, refletindo o compromisso da Unidade de Apoio ao 
        Ensino e à Pesquisa em promover uma formação de qualidade, que atenda às demandas complexas e dinâmicas da instituição. Através dessa 
        iniciativa, o Complexo Hospitalar da UFC reafirma seu papel como um centro de referência na formação de profissionais de saúde, 
        contribuindo significativamente para a melhoria dos indicadores de saúde e para a segurança das pacientes atendidas.
    """)

    # Carregar os dados do CSV
    df_participantes = pd.read_csv("Assets/dataSets/participantes_por_categoria.csv")

    # Remover a linha do total
    df_participantes = df_participantes[df_participantes['Categoria'] != 'TOTAL']

    # Criar o gráfico de barras
    fig_participantes = go.Figure(data=[
        go.Bar(
            x=df_participantes['Quantitativo'],
            y=df_participantes['Categoria'],
            orientation='h',
            marker=dict(color='#003F36', line=dict(color='#003F36', width=1)),
            text=df_participantes['Quantitativo'],
            textposition='outside'
        )
    ])

    fig_participantes.update_layout(
        title='Número de participantes por categoria',
        xaxis_title='Quantitativo',
        yaxis_title='Categoria',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_participantes)

    st.markdown("""
        ##### Principais registros do curso
    """)

    # Centralizar e exibir as imagens
    st.image("Assets/Images/suporteAvancadoObst1.jpg", width=500, caption='Informativo do curso.')
    st.image("Assets/Images/suporteAvancadoObst2.jpg", width=500, caption='Atividades realizados durante o curso.')

    st.markdown("""
        Além deste curso a unidade promoveu uma capacitação para formação de bombeiros resgatistas, quanto a emergências obstétricas. 
        Capacitando 28 bombeiros.
    """)

    st.markdown("""
        ##### Coordenação de Práticas em Cenários de Simulação 
    """)

    st.markdown("""
        A UAEP foi responsável pela produção de dois novos cenários de práticas em simulação, na área de ginecologia e obstetrícia: 
        Assistência ao nascimento/ delivramento placentário ativo e Bloqueio do Nervo Pudendo.

        Dentre o conjunto de cenários de simulação, coordenados pela UEAP, estão:
        - Assistência ao nascimento/ delivramento placentário ativo;
        - Bloqueio do Nervo Pudendo;
        - Treinamento de parto com fórceps;
        - Treinamento de Parto pélvico;
        - Parto pélvico/ fórceps piper;
        - Treinamento Parto.

        O número total de residentes, prof. do Corpo clínico / colaborador do CH-UFC/Ebserh, participantes em pelo menos um dos cenários 
        descritos acima, por período, está destacado no gráfico abaixo. Vale ressaltar que o gráfico abaixo não representa todos os cenários 
        de práticas disponíveis, apenas aqueles referentes a área de ginecologia e obstetrícia.
    """)

    # Carregar os dados do CSV do gráfico de linha
    df_ginecologia = pd.read_csv("Assets/dataSets/ginecologia_obstetricia.csv")

    # Criar o gráfico interativo de linha
    fig_ginecologia = go.Figure(data=go.Scatter(
        x=df_ginecologia['Período'],
        y=df_ginecologia['Participantes'],
        mode='lines+markers+text',
        line=dict(color='#003F36', width=2),
        marker=dict(size=8, color='#003F36', line=dict(width=2, color='white')),
        text=df_ginecologia['Participantes'],
        textposition='top center'
    ))

    fig_ginecologia.update_layout(
        title='Número de participantes em pelo menos um dos cenários de práticas em simulação da área de ginecologia e obstetrícia (2023)',
        xaxis_title='Período (2023)',
        yaxis_title='Nº de participantes',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_ginecologia)

def gestao_pesquisa_inovacao():
    image_path_taina = "Assets/Images/taina.png"
    image_base64_setor_inovacao = get_image_as_base64(image_path_taina)

    st.markdown(
        f"""
        <style>
        .centered-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 50%;
            width: 180px;
        }}
        </style>
        <img src="data:image/png;base64,{image_base64_setor_inovacao}" class="centered-img">
        """,
        unsafe_allow_html=True
    )
    st.header("Setor de Gestão da Pesquisa e Inovação Tecnológica")
    st.markdown("""
        Em 2023, o Setor de Gestão da Pesquisa e Inovação Tecnológica em Saúde (SGPITS) dedicou-se a fomentar e aumentar a visibilidade das 
        produções científicas e tecnológicas do CH-UFC. Em alinhamento com o PDE finalizado em 2023, o SGPTIS implantou um fluxo para 
        monitoramento das captações de novas pesquisas clínicas. Além disso, diversos eventos científicos foram realizados, abrangendo a 
        comunidade do interna e externa ao Complexo. Estão vinculadas ao SGPITS a Unidade de Gestão da Pesquisa (UGPESQ) e a Unidade de Gestão da 
        Inovação Tecnológica em Saúde (UGITS). Tais unidades atuam no desenvolvimento de pesquisas clínicas e acadêmicas, bem como na elaboração 
        de estudos de avaliação de tecnologias em saúde que apoiam a assistência e a gestão baseada em evidências.
    """)

def unidade_gestao_pesquisa():
    st.header("Unidade de Gestão da Pesquisa")
    st.markdown("""
        A Unidade de Gestão da Pesquisa (UGPESQ), enquanto incentivadora do desenvolvimento tecnológico, tem contribuído de maneira crescente 
        no fomento de pesquisas no âmbito local, nacional e internacional. Além de estudos acadêmicos de graduação e pós-graduação das áreas 
        da saúde, realiza estudos clínicos envolvendo a análise de eficácia e segurança de medicações. 

        O estímulo à pesquisa no CH-UFC pode ser observado pelo volume de estudos acadêmicos conduzidos em diversas etapas educacionais, 
        incluindo graduação, residências em saúde, mestrado e doutorado. Após queda no número de pesquisas de cunho acadêmico observada nos 
        anos de pandemia de Covid-19 (2020 e 2021), a retomada das atividades dos pesquisadores tem resultado em aumento progressivo desde 2022. 
        Em 2023, foram registradas 217 pesquisas acadêmicas desenvolvidas no âmbito do CH-UFC, um aumento de 25% em relação a 2021 e 7% em 
        relação a 2022 (ver figura abaixo).
    """)

     # Carregar os dados do CSV
    df_pesquisas = pd.read_csv("Assets/dataSets/pesquisas_academicas.csv")

    # Criar o gráfico de barras
    fig_pesquisas = go.Figure(data=[
        go.Bar(
            x=df_pesquisas['Ano'],
            y=df_pesquisas['Pesquisas'],
            marker=dict(color='#003F36', line=dict(color='#003F36', width=1)),
            text=df_pesquisas['Pesquisas'],
            textposition='outside'
        )
    ])

    fig_pesquisas.update_layout(
        title='Pesquisas acadêmicas iniciadas no Complexo Hospitalar da UFC/EBSERH (2013-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Pesquisas',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_pesquisas)

    st.markdown("""
        Digno de nota, desde maio de 2022, todas as pesquisas acadêmicas e clínicas realizadas no CH-UFC estão cadastradas no Sistema Rede 
        Pesquisa, sistema de gerenciamento de pesquisas desenvolvidas nos hospitais da Rede Ebserh, contribuindo para a construção de indicadores 
        de gestão. 

        Quanto às pesquisas clínicas, desenvolvidas com fomento externo, é possível observar um aumento de 17,74% no número de novas pesquisas 
        iniciadas em 2023 quando comparada ao ano anterior, conforme tabela abaixo. Pode-se concluir, também, que, a partir da análise das 
        especialidades contempladas pelas pesquisas, houve expansão das áreas terapêuticas envolvidas, o que denota maior engajamento de 
        pesquisadores das diversas áreas, incluindo jovens pesquisadores, o que fortalece a perenidade do CH-UFC como um centro de excelência em 
        pesquisa.
    """)

     # Carregar os dados do CSV de pesquisas clínicas
    df_pesquisas_clinicas = pd.read_csv("Assets/dataSets/pesquisas_clinicas.csv")

    # Mostrar o DataFrame no Streamlit
    st.markdown("### Tabela de Pesquisas Clínicas com Fomento Externo")
    st.dataframe(df_pesquisas_clinicas)

    # Criar o gráfico de barras empilhadas
    fig_pesquisas_clinicas = go.Figure()

    especialidades = df_pesquisas_clinicas['Especialidade'].unique()
    anos = df_pesquisas_clinicas.columns[1:]

    for especialidade in especialidades:
        df_especialidade = df_pesquisas_clinicas[df_pesquisas_clinicas['Especialidade'] == especialidade]
        fig_pesquisas_clinicas.add_trace(go.Bar(
            x=anos,
            y=df_especialidade[anos].values[0],
            name=especialidade
        ))

    fig_pesquisas_clinicas.update_layout(
        barmode='stack',
        title='Pesquisas clínicas com fomento externo realizadas na UGPESQ/CH-UFC por especialidade<br> (2013-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Pesquisas',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_pesquisas_clinicas)

    st.markdown("""
        Além das 62 pesquisas iniciadas em 2023, outras 22 tiveram o processo de contrato iniciado em 2023, tendo início previsto para o ano de 
        2024 conforme tabela abaixo. 
    """)

    # Carregar os dados do CSV de pesquisas previstas para 2024
    df_pesquisas_2024 = pd.read_csv("Assets/dataSets/pesquisas_previstas_2024.csv")

    # Mostrar o DataFrame no Streamlit
    st.markdown("##### Tabela de Pesquisas Clínicas com Fomento Externo Previstas para 2024")
    st.dataframe(df_pesquisas_2024)

    st.markdown("""
        Nos últimos anos, diversas ações foram tomadas no sentido de aumentar o número de pesquisas realizadas no CH-UFC, dentre as quais 
        destacamos: 
                
        1. Melhorias na infraestrutura, na qualificação de recursos humanos e nos processos da Unidade de Pesquisa Clínica;
        2. Solidificação do Núcleo de Apoio ao Pesquisador, que fornece suporte estatístico, regulatório e bibliotecário;
        3. Realização de eventos periódicos de formação e divulgação da pesquisa;
        4. Adesão ao Programa de Iniciação Científica (PIC) e Iniciação Tecnológica (PIT) da Ebserh, em parceria com o CNPq;
        5. Implantação de um processo de captação de pesquisas clínicas, projeto formalizado no PDE.103 (2021-2023), que contou com as 
        seguintes entregas: 
        - Reformulação do fluxo de captação e monitoramento da captação de pesquisas clínicas;
        - Estruturação do Núcleo de Captação, Desenvolvimento e Apoio a Projetos de Pesquisa e Inovação;
        - Criação de um portfólio da Unidade de Pesquisa clínica, disponível no link https://sway.cloud.microsoft/ErU89Gm728kQuwU2?ref=Link.

        Para garantir a celeridade, conformidade e o bom andamento das pesquisas desenvolvidas no CH-UFC, pode-se contar com dois Comitês de 
        Ética em Pesquisa (CEP): o CEP do Hospital Universitário Walter Cantídio (HUWC) e o CEP da Maternidade Escola Assis Chateaubriand 
        (MEAC). A figura abaixo ilustra o número anual de projetos avaliados pelos dois CEPs.
    """)

    # Carregar os dados do CSV de projetos avaliados
    df_projetos_avaliados = pd.read_csv("Assets/dataSets/projetos_avaliados.csv")

    # Criar o gráfico de linhas
    fig_projetos_avaliados = go.Figure()

    fig_projetos_avaliados.add_trace(go.Scatter(
        x=df_projetos_avaliados['Ano'],
        y=df_projetos_avaliados['HUWC'],
        mode='lines+markers+text',
        name='HUWC',
        line=dict(color='#003F36', width=2),
        text=df_projetos_avaliados['HUWC'],
        textposition='top center'
    ))

    fig_projetos_avaliados.add_trace(go.Scatter(
        x=df_projetos_avaliados['Ano'],
        y=df_projetos_avaliados['MEAC'],
        mode='lines+markers+text',
        name='MEAC',
        line=dict(color='#9ACD32', width=2),
        text=df_projetos_avaliados['MEAC'],
        textposition='top center'
    ))

    fig_projetos_avaliados.update_layout(
        title='Número de projetos avaliados pelos Comitês de Ética do Complexo Hospitalar da UFC (2013-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Projetos',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_projetos_avaliados)

def apoio_pesquisador():
    st.header("Núcleo de apoio ao pesquisador")
    st.markdown("""
        A fim de assessorar as atividades de pesquisas acadêmicas e clínicas, a UGPESQ conta com o Núcleo de Apoio ao Pesquisador (NAP). O NAP 
        é formado por três profissionais:
	
        - Estatístico: instrumentaliza e suporta pesquisadores e estudantes quanto à coleta e análise de dados, assim como quanto à 
        interpretação de resultados. Dentre os instrumentos utilizados, está a plataforma Redcap. 
        - Assistente de regulatório: dá suporte às submissões regulatórias, desde as tramitações locais (Comissão de Regulamentação e Análise 
        de Pesquisas – CRAP) à submissão dos documentos ao sistema CEP/CONEP via Plataforma Brasil.
        - Bibliotecária: instrui e dá suporte aos pesquisadores e estudantes quanto às estratégias de busca bibliográfica e normatização, bem 
        como gerencia as consultas aos prontuários. Além disso, dá suporte aos pesquisadores para construção e atualização do currículo na 
        plataforma Lattes.

        A figura abaixo mostra o aumento progressivo no número de pesquisadores assistidos pelo NAP desde sua fundação até 2023, com um pico 
        em 2022, em virtude de uma demanda reprimida no período da pandemia. 
    """)

    # Carregar os dados do CSV
    df_pesquisadores = pd.read_csv("Assets/dataSets/quantitativo_pesquisadores.csv")

    # Criar o gráfico de barras
    fig_pesquisadores = go.Figure(data=[
        go.Bar(
            x=df_pesquisadores['Ano'],
            y=df_pesquisadores['Quantitativo'],
            marker=dict(color='#003F36', line=dict(color='#003F36', width=1)),
            text=df_pesquisadores['Quantitativo'],
            textposition='outside'
        )
    ])

    fig_pesquisadores.update_layout(
        title='Quantitativo de pesquisadores atendidos pelo NAP (2015-2023)',
        xaxis_title='Ano',
        yaxis_title='Número de Pesquisadores',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_pesquisadores)

    st.markdown("""
        Na figura abaixo, está ilustrada a distribuição dos atendimentos realizados por cada profissional do NAP ao longo de 2023.
    """)

    # Carregar os dados do CSV dos atendimentos em 2023
    df_atendimentos = pd.read_csv("Assets/dataSets/atendimentos_nap_2023.csv")

    # Criar o gráfico de barras
    fig_atendimentos = go.Figure(data=[
        go.Bar(
            x=df_atendimentos['Area'],
            y=df_atendimentos['Quantidade'],
            marker=dict(color='#003F36', line=dict(color='#003F36', width=1)),
            text=df_atendimentos['Quantidade'],
            textposition='outside'
        )
    ])

    fig_atendimentos.update_layout(
        title='Número médio de atendimento por mês do NAP por área de apoio (2023)',
        xaxis_title='Área de Apoio',
        yaxis_title='Número de Atendimentos',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_atendimentos)

def redcap():
    st.header("Research Eletronic Data Capture – REDCap")
    st.markdown("""
        Em outubro de 2018, a UGPESQ, em colaboração com a Unidade e-Saúde, aderiu à plataforma REDCap, uma plataforma de coleta e 
        gerenciamento de dados para pesquisas clínicas e de saúde, oferecendo personalização, segurança, facilidade de uso, colaboração, 
        rastreabilidade, suporte para vários tipos de dados e conformidade regulatória na gestão de dados dos pesquisadores que atuam no 
        Complexo. A implementação bem-sucedida do REDCap no CH-UFC não apenas melhorou significativamente a qualidade das pesquisas, como 
        estimulou sua replicação e disseminação em toda a rede EBSERH. 

        O NAP teve um papel essencial nesse avanço, oferecendo treinamento especializado em REDCap através da plataforma 3Ec para toda a Rede 
        Ebserh, sob a orientação de seu estatístico. Este curso já atraiu mais de 1000 inscritos, demonstrando claramente a importância do NAP 
        em capacitar profissionais para a coleta e análise de dados em pesquisas de saúde, promovendo uma cultura de excelência em pesquisa 
        dentro da EBSERH.
    """)

def infraestrutura():
    st.header("Infraestrutura")
    st.markdown("""
        Além do espaço físico, que inclui:
        - Auditório;
        - Biblioteca virtual;
        - Salas de reuniões;
        - Salas de monitorias;
        - Consultórios;
        - Enfermarias;
        - Farmácia com acesso restrito e controle de temperatura;
        - Sala de coleta e área de processamento de amostras, 
        
        A Unidade de Pesquisa Clínica oferece aos pesquisadores equipamentos multiusuários para a realização de pesquisas. Estes equipamentos incluem: 
        - Carrinho de emergência com monitor multiparamétrico;
        - Bombas de infusão;
        - Eletrocardiógrafo;
        - Centrífuga refrigerada;
        - Microcentrífuga;
        - Estufa/incubadora;
        - Homogeneizador;
        - Capela de fluxo laminar;
        - Geladeira (2 a 8 o.C);
        - Freezer (-20 ºC) e ultrafreezer (-80 ºC).
                
        Além disso, a UGPESQ conta com um aparelho de ultrassonografia, uma balança de bioimpedância e um equipamento de densitometria óssea, localizados no Laboratório de Metabologia.
    """)

    st.image("Assets/Images/infraestrutura1.jpg", caption='Infraestrutura e equipamentos da UGPESQ.")

    st.markdown("""
        Em 2023, foram adquiridas uma impressora 3D e uma cama de tilt test, ampliando a infraestrutura oferecida aos pesquisadores. 

        Ademais, está em andamento um Projeto de Desenvolvimento Institucional (PDI), que prevê reestruturação e melhorias no auditório.
    """)

def revista_medicina():
    st.header("Revista de medicina da UFC")
    st.markdown("""
        A Revista de Medicina da UFC foi criada em 1961 e, após um período de interrupção temporária em suas publicações (2001 a 2013), em 
        2014, retomou sua periodicidade contando com o fundamental apoio da Gerência de Ensino e Pesquisa (GEP) do CH-UFC/EBSERH. O periódico 
        tem contribuído para a divulgação e o desenvolvimento da pesquisa científica da área médica e ciências afins.

        O público-alvo principal da revista são estudantes de graduação e pós-graduação em medicina e ciências correlatas, médicos residentes, 
        assistentes e docentes de universidades. A revista proporciona acesso público a todo seu conteúdo, possibilitando um maior intercâmbio 
        de conhecimento e despertando o incentivo à leitura e à citação dos artigos. 

        No final de 2022 foi divulgada a avaliação QUALIS quadrienal da Revista de Medicina da UFC. Antes classificada como B5 na área de 
        Ensino, C em Medicina I e Medicina II e B4 para Saúde Coletiva, obteve nova classificação, avançando para o nível B3 nas áreas: 
        Ciências Biológicas II, Educação física, Enfermagem, Ensino, Interdisciplinar, Medicina I, Medicina II, Medicina III, Nutrição, 
        Odontologia, Psicologia e Saúde Coletiva. 

        No ano de 2023 foram submetidos 139 artigos, o que representa um aumento de 30% no número de submissões em relação ao ano anterior, 
        com 43 publicações, as quais ocorrem em fluxo contínuo desde 2022.

        Na tabela abaixo, podem ser observados os indicadores da Revista de Medicina da UFC no período entre 2015 e 2023.
    """)

    # Carregar os dados do CSV
    df_indicadores = pd.read_csv("Assets/dataSets/indicadores_revista_medicina.csv")

    # Criar o gráfico de linhas
    fig_indicadores = go.Figure()

    for i, row in df_indicadores.iterrows():
        fig_indicadores.add_trace(go.Scatter(
            x=df_indicadores.columns[1:],
            y=row[1:],
            mode='lines+markers+text',
            name=row['Indicadores'],
            text=row[1:],
            textposition='top center'
        ))

    fig_indicadores.update_layout(
        title='Indicadores de Resultados da Revista de Medicina UFC (2015-2023)',
        xaxis_title='Ano',
        yaxis_title='Quantidade',
        template='plotly_white'
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig_indicadores)

def unidade_gestao_inovacao():
    st.header("Unidade de Gestão da Inovação Tecnológica em Saúde")
    st.markdown("""
        A Unidade de Gestão da Inovação Tecnológica em Saúde (UGITS) tem como objetivo primordial a produção de conhecimento técnico-científico e 
        apoio aos processos de inovação tecnológica em saúde. Essa produção visa aprimorar o processo decisório relacionado às tecnologias em 
        saúde, buscando uma eficiência maior em todas as etapas. No contexto do CH-UFC/EBSERH, a UGITS desempenha um papel fundamental ao 
        desenvolver iniciativas que fornecem suporte à tomada de decisão sobre a incorporação, modificação ou exclusão dessas tecnologias na 
        instituição.
                
        A Unidade tem ainda participação ativa nas Comissões de apoio à incorporação de tecnologias em saúde no CH-UFC/EBSERH, tais como: Farmácia 
        e Terapêutica (HUWC e MEAC) e Padronização de Produtos para Saúde atuando principalmente na elaboração de documentos técnicos científicos 
        que apoiem a decisão de incorporação. Colaborou com a elaboração do Guia Farmacoterapêutico do CH-UFC 2023-2024, conforme figura abaixo.
    """)

    st.image("Assets/Images/guiafarmacoterapeutico.jpg", caption='Guia Farmacoterapêutico do CH-UFC 2023/2024.')

    st.markdown("""
        Com o propósito de apoiar o desenvolvimento e implantação de Núcleos de Avaliação de Tecnologias em Saúde da rede Ebserh, a UGITS 
        contribuiu com a elaboração da política de Avaliação de Tecnologias em Saúde da Rede Ebserh e de um Guia para Organização e Funcionamento 
        dos Núcleos de Avaliação de Tecnologias em Saúde da Rede Ebserh, visando ao fortalecimento da atuação dos Núcleos de Avaliação de 
        Tecnologias em Saúde (NATS). Adicionalmente, participou de um grupo de trabalho para elaboração da Diretriz de nota técnica de revisão 
        rápida em parceria com a Rede Brasileira de Avaliação de Tecnologias em Saúde/MS. Em outubro de 2023 o NATS CH-UFC foi eleito como 
        representante suplente da região Nordeste da Rede Brasileira de Avaliação de Tecnologias na Saúde (2024 – 2025).
    """)

    st.image("Assets/Images/guiafuncionamentoNATS.jpg", caption='Guia para organização e funcionamento dos núcleos de avaliação de tecnologias em saúde da rede Ebserh.')
        
    st.markdown("""
        Como atividade de ensino, visando maior engajamento dos cursos na área da pesquisa e inovação e gerando a perspectiva da formação de 
        profissionais com melhor conhecimento na área supracitada, em 2023, foi ministrada disciplina de pesquisa e inovação em saúde, com 
        ênfase na prática da saúde baseada em evidência na pós-graduação (Residência multidisciplinar em saúde do CH-UFC).

        A UGITS, vem desenvolvendo, através do Núcleo de Avaliação de Tecnologias em Saúde, o Estudo Observacional Brasileiro em crianças com 
        AME 5q (SOBRE5) com objetivo de avaliar a efetividade, segurança e análise econômica do uso de uma Terapia Gênica para crianças com 
        Atrofia Muscular Espinhal, uma parceria da EBSERH e Ministério da Saúde. Além de estudos com alunos de graduação através dos programas 
        de iniciação científica e tecnológica da rede Ebserh.

        Em 2023, foram emitidas 71 notas técnicas em atendimento ao Termo de Cooperação Técnica com o Tribunal de Justiça do Estado do Ceará 
        (Termo de Cooperação 02/2021). A referida cooperação ocorre desde 2016 com objetivo de contribuir na elaboração de documentos técnicos 
        e especializados na área da saúde visando auxiliar magistrados das Varas da Fazenda Pública, do Tribunal de Justiça, dos Juizados 
        Especiais da Fazenda Pública e da Turma Recursal da Fazenda Pública. Além de 7 pareceres técnicos científicos para apoiar a decisão 
        acerca de incorporação de tecnologias em saúde no CHUFC.
    """)

def programas_iniciacao():
    st.header("Programas de Iniciação Científica e Tecnológica da Ebserh/CNPq")
    st.markdown("""
        Em 2022, foi lançado o Programa de Iniciação Científica (PIC) da Ebserh, em parceria com o CNPq. Na primeira edição do PIC, o CH-UFC 
        foi a instituição da rede Ebserh com o maior número de inscritos, sendo contemplado com 10 bolsas. Na edição de 2023, houve um 
        incremento no número de bolsas, beneficiando 16 estudantes e seus respectivos orientadores. 

        Em 2023, foi lançado o Programa de Iniciação Tecnológica (PIT) da Ebserh/CNPq, com pronta adesão do CH-UFC, o qual foi beneficiado com 
        11 bolsas. 

        O objetivo destes bem-sucedidos programas é o de atender alunos dos cursos de graduação da Universidade Federal do Ceará com projetos 
        relacionados à área da saúde desenvolvidos no Complexo Hospitalar, estimulando seu desenvolvimento pessoal e profissional, bem como 
        seu envolvimento em conhecimentos, práticas e metodologias atrelados ao desenvolvimento e processos próprios do saber científico e 
        tecnológico, além das suas potencialidades de pesquisa, desenvolvimento e inovação.

        Como resultados desses projetos, apresentados no II Congresso de Ensino, Pesquisa e Assistência do CH-UFC, foram registados 35 
        palestrantes, 105 participantes e 83 trabalhos apresentados na forma de temas livres orais e posters.

        Nas figuras abaixo, constam os banners de divulgação dos editais, bem como os eventos de acompanhamento dos projetos dos programas PIC 
        e PIT.
    """)

    st.image("Assets/Images/PIT1.jpg", caption='Banner para divulgação do PIT 2023.')
    st.image("Assets/Images/PIC1.jpg", caption='Banner para divulgação do PIC 2023.')
    st.image("Assets/Images/encontroPIC.png", caption='Banner para divulgação do II Encontro do PIC (2023).')
    st.image("Assets/Images/encerramentoPIC.jpg", caption='Foto deste evento, com encerramento da primeira turma PIC (2022).')
    st.image("Assets/Images/PITePIC.jpg", caption='Banner para divulgação do III Encontro do PIC e II Encontro PIT (2023).')


def eventos():
    st.header("Eventos")
    st.markdown("""
        Em 2023, o Setor de Gestão da Pesquisa e Inovação Tecnológica investiu em iniciativas voltadas para o ensino nas áreas de Pesquisa 
        Clínica e Inovação Tecnológica em Saúde. Ao longo do ano foram realizados, encontros, cursos e congresso voltado para esta temática. 

        Em maio foi promovido o II Encontro do PIC onde os bolsistas tiveram oportunidade de apresentar os trabalhos desenvolvidos durante o 
        programa para um comitê avaliativo. 

        Em dezembro foi realizado o II PIT e III PIC e o II Congresso de Ensino, Pesquisa e Assistência do CH-UFC/EBSERH.
    """)
    st.image("Assets/Images/congressoEnsinoPesquisa.jpg", caption='Folder de divulgação do II Congresso de Ensino, Pesquisa e Assistência do CH-UFC/EBSERH (2023).')

    st.markdown("""
        Além disso, foi organizado o II Simpósio de Pesquisa Clínica e Inovação Tecnológica, bem como o 3° minicurso de pesquisa científica, tendo 
        como principais temas: Pesquisas nas principais bases de dados, gerenciamento de referências bibliográficas, seleção de periódicos para 
        publicação/fator de impacto e Qualis, processo editorial/da submissão à publicação e preenchimento de currículo lattes. Realizados na 
        modalidade remota, esses eventos possibilitaram a disseminação de conteúdos relevantes relacionados à Pesquisa e Inovação, tanto entre 
        colaboradores do CH-UFC/EBSERH como também profissionais da saúde e estudantes pertencentes instituições de outros Estados.
    """)

def unidade_esaude():
    st.header("Unidade de e-saúde")
    st.markdown("""
        Em 2023, a Unidade de E-Saúde da UFC concretizou a implementação de um estúdio multiuso, projetado para alinhar-se ao seguinte objetivo: 
        uso de tecnologias avançadas de informática e telecomunicações para facilitar a troca de informações entre profissionais de saúde, 
        melhorando a disponibilidade de diagnósticos e tratamentos aos pacientes.
                
        ##### Infraestrutura do Estúdio
                
        O estúdio é equipado com tecnologia de ponta para produção de conteúdos digitais que suportam a missão de e-saúde, conforme listado 
        abaixo:
        - Computador PC GAMER com aceleração de vídeo;
        - Notebook GAMER com aceleração de vídeo;
        - Mesa de corte e captura de vídeo com entrada HDMI para quatro câmeras simultâneas;
        - Placa de captura de vídeo HDMI (Entrada Simples);
        - Placa de captura de vídeo RCA (Entrada Simples);
        - Conversor de mídia SDI/HDMI;
        - Dois microfones de mão convencionais;
        - Quatro microfones de lapela sem fio, e duas bases de recepção; 
        - Mesa de som com 8 canais;
        - Câmera DSLR;
        - Câmera PTZ com 30x de zoom;
        - Tela Chroma Key;
        - Dois Softbox’s;
        - Servidor de Streaming Interno;
        - Softwares da Switch Adobe para edição de vídeos e áudios;
        - Softwares da Switch Corel para edição de imagens;
        - OBS Studio para transmissões e gravações.

        ##### Impactos e Benefícios Estratégicos para o Complexo Hospitalar da UFC
                
        O estúdio multiuso permite gravações e transmissões em tempo real diretamente de locais críticos, como salas de cirurgia, o que é 
        essencial para o ensino e a colaboração médica. Os impactos específicos incluem:

        - Melhoria da Disponibilidade de Educação Médica: O estúdio proporciona aos residentes e estudantes uma plataforma para assistir a 
        procedimentos médicos ao vivo, melhorando o aprendizado e o treinamento clínico através de experiências práticas e interativas.
        - Facilitação da Colaboração Interdisciplinar: Promove a troca de informações e consultas em tempo real entre especialistas, 
        enriquecendo os diagnósticos e tratamentos.
        - Ampliação do Acesso a Recursos Médicos: O estúdio permite a disseminação de conhecimento médico especializado para profissionais em 
        regiões remotas, contribuindo para a equidade no acesso à saúde.
        - Documentação e Análise para Melhoria Contínua: Auxilia na documentação detalhada de procedimentos médicos que podem ser revisados e 
        estudados para aprimorar as práticas clínicas.
        
        A primeira demonstração do potencial do estúdio ocorreu em agosto de 2023 com a transmissão ao vivo de uma cirurgia de hérnia de disco, validando a integração da telemedicina no ambiente acadêmico e clínico. A continuidade desse projeto reforça o compromisso da UFC com a inovação na educação e no tratamento médico, alinhando-se perfeitamente ao objetivo estratégico da área de e-saúde.

    """)

# Função para definir qual função executar com base na seleção
def display_selected(selected):
    if selected == "Apresentação":
        apresentacao()
    elif selected == "1 Gerência de Ensino e Pesquisa (GEP)":
        gep()
    elif selected == "2 Setor de Gestão do Ensino":
        setor_gestao_ensino()
    elif selected == "2.1 Unidade de Gestão de Pós-Graduação":
        unidade_gestao_pos_graduacao()
    elif selected == "2.1.1 Atividades de Residência Médica":
        atividades_residencia_medica()
    elif selected == "2.1.2 Atividades de Residência Multiprofissional e Uniprofissional da Saúde":
        atividades_residencia_multiprofissional()
    elif selected == "2.1.3 Participação no Plano Diretor Estratégico 2021-2023":
        participacao_plano_diretor()
    elif selected == "2.2 Unidade de Gestão de Graduação, Ensino Técnico e Extensão":
        unidade_gestao_graduacao()
    elif selected == "2.2.1 Estágios obrigatórios - Graduação Multiprofissional":
        estagios_obrigatorios_graduacao_multiprofissional()
    elif selected == "2.2.2 Estágios obrigatórios - Graduação Médica":
        estagios_obrigatorios_graduacao_medica()
    elif selected == "2.2.3 Controle e regulação de estágios de graduação":
        controle_regulacao_estagios()
    elif selected == "2.2.4 Estágios não obrigatório":
        estagios_nao_obrigatorios()
    elif selected == "2.2.5 Ensino baseado em Simulação":
        ensino_simulacao()
    elif selected == "2.2.6 Acervo":
        acervo()
    elif selected == "2.2.7 Inovação":
        inovacao()
    elif selected == "2.2.8 Utilização do centro de simulação":
        centro_simulacao()
    elif selected == "3 Unidade de Apoio ao Ensino e à Pesquisa":
        unidade_apoio_ensino_pesquisa()
    elif selected == "4 Setor Gestão da Pesquisa e Inovação Tecnológica":
        gestao_pesquisa_inovacao()
    elif selected == "4.1 Unidade de Gestão da Pesquisa":
        unidade_gestao_pesquisa()
    elif selected == "4.1.1 Núcleo de apoio ao pesquisador":
        apoio_pesquisador()
    elif selected == "4.1.2 Research Eletronic Data Capture – REDCap":
        redcap()
    elif selected == "4.1.3 Infraestrutura":
        infraestrutura()
    elif selected == "4.1.4 Revista de medicina da UFC":
        revista_medicina()
    elif selected == "4.2 Unidade de Gestão da Inovação Tecnológica em Saúde":
        unidade_gestao_inovacao()
    elif selected == "4.2.1 Programas de Iniciação Científica e Tecnológica da Ebserh/CNPq":
        programas_iniciacao()
    elif selected == "4.3 Eventos":
        eventos()
    elif selected == "5 Unidade de e-saúde":
        unidade_esaude()

# Função principal para o app
def main():
    st.sidebar.title("Menu de Navegação")

    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        color: #444;
    }
    .sidebar .sidebar-content a {
        color: #007bff;
        text-decoration: none;
    }
    .sidebar .sidebar-content a:hover {
        color: #0056b3;
    }
    .sidebar .sidebar-content .selected {
        color: #fff;
        background-color: #78F4E2;
        border-radius: 4px;
        padding: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

    menu_items = {
        "Apresentação": [],
        "1 Gerência de Ensino e Pesquisa (GEP)": [],
        "2 Setor de Gestão do Ensino": [],
        "2.1 Unidade de Gestão de Pós-Graduação": [],
        "2.1.1 Atividades de Residência Médica": [],
        "2.1.2 Atividades de Residência Multiprofissional e Uniprofissional da Saúde": [],
        "2.1.3 Participação no Plano Diretor Estratégico 2021-2023": [],
        "2.2 Unidade de Gestão de Graduação, Ensino Técnico e Extensão": [],
        "2.2.1 Estágios obrigatórios - Graduação Multiprofissional":[],
        "2.2.2 Estágios obrigatórios - Graduação Médica": [],
        "2.2.3 Controle e regulação de estágios de graduação": [],
        "2.2.4 Estágios não obrigatório": [],
        "2.2.5 Ensino baseado em Simulação": [],
        "2.2.6 Acervo": [],
        "2.2.7 Inovação": [],
        "2.2.8 Utilização do centro de simulação": [],
        "3 Unidade de Apoio ao Ensino e à Pesquisa": [],
        "4 Setor Gestão da Pesquisa e Inovação Tecnológica": [],
        "4.1 Unidade de Gestão da Pesquisa": [],
        "4.1.1 Núcleo de apoio ao pesquisador": [],
        "4.1.2 Research Eletronic Data Capture – REDCap": [],
        "4.1.3 Infraestrutura": [],
        "4.1.4 Revista de medicina da UFC": [],
        "4.2 Unidade de Gestão da Inovação Tecnológica em Saúde": [],
        "4.2.1 Programas de Iniciação Científica e Tecnológica da Ebserh/CNPq": [],
        "4.3 Eventos": [],
        "5 Unidade de e-saúde": [],
    }

    selected_main = st.sidebar.radio("Selecione a Seção", list(menu_items.keys()))

    display_selected(selected_main)

if __name__ == "__main__":
    main()
