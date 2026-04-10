#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SistemaPerfilAcesso:
    def __init__(self):
        self.perfis = {
            'PERFIL_USUARIO_COMUM': {
                'gerais': [
                    'Consultas → Consulta Qualificação',
                    'Consultas → Consulta de Renda Atualizada Automaticamente (CNIS)',
                    'Consultas → Consulta de escolaridade atualizada (Sistema Presença)',
                    'Painéis → Painel Gerencial Consulta',
                    'Mural de Comunicação → Visão Geral',
                    'Família → Buscar → Buscar Família',
                    'Família → Buscar → Buscar Família/Pessoas em Cadastramento',
                    'Família → Buscar → Família Sem Registro Civil',
                    'Família → Buscar → Pessoas Aguardando CPF',
                    'Família → Buscar → Pessoas com Indicativo de Óbito',
                    'Família → Buscar → Família com Indicação RL',
                    'Família → Visualizar Família → Visualizar Histórico Família',
                    'Família → Visualizar Família → Visualizar Histórico Pessoa',
                    'Família → Visualizar Família → Consultar Pessoas Transferidas',
                    'Família → Visualizar Família → Painel da Família',
                    'Família → Visualizar Família → Consulta renda integração CNIS',
                    'Família → Visualizar Família → Baixar Formulários',
                    'Família → Visualizar Família → Exportar CSV Histórico Pessoa',
                    'Família → Visualizar Família → Exportar CSV Histórico Família'
                ],
                'municipal': [
                    'Família → Visualizar Família → Impressão de Renda CNIS',
                    'Questionários → Responder/Consultar/Visualizar Questionário Qualificação 2024 e 2025',
                    'Unidade Territorial Local → Buscar UTL',
                    'Entrevistas Offline → Buscar Entrevistas',
                    'Entrevistas Offline → Importar Entrevistas',
                    'Entrevistas Offline → Visualizar Entrevistas',
                    'Família → Incluir → Incluir Família',
                    'Família → Incluir → Transferir Família',
                    'Família → Continuar Inclusão/Alterar Família → Emissão Termo Adesão Envio de Mensagens',
                    'Família → Continuar Inclusão/Alterar Família → Emissão Termo Família Unipessoal',
                    'Família → Continuar Inclusão/Alterar Família → Incluir Pessoa',
                    'Família → Continuar Inclusão/Alterar Família → Excluir Pessoa',
                    'Família → Continuar Inclusão/Alterar Família → Transferir Família',
                    'Família → Continuar Inclusão/Alterar Família → Transferir Pessoa',
                    'Família → Visualizar Família → Emissão Folha Resumo',
                    'Família → Visualizar Família → Emissão Comprovante Cadastro',
                    'Família → Visualizar Família → Emissão Comprovante Prestação de Informações',
                    'Família → Visualizar Família → Excluir Família',
                    'Família → Visualizar Família → Confirmar Cadastro',
                    'Família → Visualizar Família → Trocar Responsável Familiar',
                    'Família → Visualizar Família → Excluir Representante Legal',
                    'Família → Visualizar Família → Incluir Representante Legal',
                    'Família → Visualizar Família → Download Documento Unipessoal'
                ],
                'estadual': [],
                'federal': [
                    'Família → Visualizar Família → Download Documento Unipessoal',
                    'Questionários → Consultar/Visualizar Questionário Qualificação 2024 e 2025'
                ]
            },
            'PERFIL_GESTOR': {
                'gerais': [
                    'Consultas → Consulta Qualificação',
                    'Consultas → Consulta de Renda Atualizada Automaticamente (CNIS)',
                    'Consultas → Consulta de escolaridade atualizada (Sistema Presença)',
                    'Painéis → Painel Gerencial Consulta',
                    'Mural de Comunicação → Visão Geral',
                    'Família → Buscar → Buscar Família',
                    'Família → Buscar → Buscar Família/Pessoas em Cadastramento',
                    'Família → Buscar → Família Sem Registro Civil',
                    'Família → Buscar → Pessoas Aguardando CPF',
                    'Família → Buscar → Pessoas com Indicativo de Óbito',
                    'Família → Buscar → Família com Indicação RL',
                    'Família → Visualizar Família → Visualizar Histórico Família',
                    'Família → Visualizar Família → Visualizar Histórico Pessoa',
                    'Família → Visualizar Família → Consultar Pessoas Transferidas',
                    'Família → Visualizar Família → Painel da Família',
                    'Família → Visualizar Família → Consulta renda integração CNIS',
                    'Família → Visualizar Família → Baixar Formulários',
                    'Família → Visualizar Família → Exportar CSV Histórico Pessoa',
                    'Família → Visualizar Família → Exportar CSV Histórico Família',
                    'Família → Buscar → Exportar CSV/XLSX: Família com Indicação RL',
                    'Família → Buscar → Exportar CSV/XLSX: Pessoas Aguardando CPF',
                    'Família → Buscar → Exportar CSV/XLSX: Famílias/Pessoas em Cadastramento',
                    'Família → Buscar → Exportar CSV/XLSX: Família Sem Registro Civil',
                    'Família → Buscar → Exportar CSV/XLSX: Pessoas com Indicativo de Óbito',
                    'Painéis → Painel Gerencial → Exportar CSV/XLSX: Relatórios Famílias Unipessoais',
                    'Painéis → Painel Gerencial → Exportar CSV/XLSX: Atualização automática de renda',
                    'Consultas → Consulta Qualificação → Exportar CSV 2025 e 2024',
                    'Consultas → Consulta de Renda (CNIS) → Exportar CSV/XLSX',
                    'Consultas → Escolaridade (Sistema Presença) → Exportar CSV/XLSX'
                ],
                'municipal': [
                    'Família → Visualizar Família → Impressão de Renda CNIS',
                    'Questionários → Responder/Consultar/Visualizar Questionário Qualificação 2024 e 2025',
                    'Unidade Territorial Local → Buscar UTL',
                    'Entrevistas Offline → Buscar Entrevistas',
                    'Entrevistas Offline → Importar Entrevistas',
                    'Entrevistas Offline → Visualizar Entrevistas',
                    'Família → Incluir → Incluir Família',
                    'Família → Incluir → Transferir Família',
                    'Família → Continuar Inclusão/Alterar Família → Emissão Termo Adesão Envio de Mensagens',
                    'Família → Continuar Inclusão/Alterar Família → Emissão Termo Família Unipessoal',
                    'Família → Continuar Inclusão/Alterar Família → Incluir Pessoa',
                    'Família → Continuar Inclusão/Alterar Família → Excluir Pessoa',
                    'Família → Continuar Inclusão/Alterar Família → Transferir Família',
                    'Família → Continuar Inclusão/Alterar Família → Transferir Pessoa',
                    'Família → Visualizar Família → Emissão Folha Resumo',
                    'Família → Visualizar Família → Emissão Comprovante Cadastro',
                    'Família → Visualizar Família → Emissão Comprovante Prestação de Informações',
                    'Família → Visualizar Família → Excluir Família',
                    'Família → Visualizar Família → Confirmar Cadastro',
                    'Família → Visualizar Família → Trocar Responsável Familiar',
                    'Família → Visualizar Família → Excluir Representante Legal',
                    'Família → Visualizar Família → Incluir Representante Legal',
                    'Família → Visualizar Família → Download Documento Unipessoal',
                    'Gestão → Entrevistadores → Buscar',
                    'Gestão → Entrevistadores → Cadastrar',
                    'Gestão → Entrevistadores → Visualizar',
                    'Gestão → Entrevistadores → Alterar',
                    'Gestão → Entrevistadores → Excluir',
                    'Gestão → Entrevistadores → Ativar/Inativar',
                    'Gestão → Entrevistadores → Visualizar Histórico',
                    'Gestão → Entrevistadores → Exportar CSV/XLSX Histórico',
                    'Gestão → Operadores → Gestão de Acesso',
                    'Unidade Territorial Local → Cadastrar',
                    'Unidade Territorial Local → Alterar',
                    'Unidade Territorial Local → Ativar/Inativar',
                    'Unidade Territorial Local → Excluir UTL',
                    'Família → Visualizar Família → Corrigir Cadastro',
                    'Consultas → Consulta da Base Mensal → Baixar Arquivo da Base Mensal'
                ],
                'estadual': [
                    'Consultas → Consulta da Base Mensal → Baixar Arquivo da Base Mensal'
                ],
                'federal': [
                    'Família → Visualizar Família → Download Documento Unipessoal',
                    'Questionários → Consultar/Visualizar Questionário Qualificação 2024 e 2025'
                ]
            },
            'PERFIL_CONSULTA': {
                'gerais': [
                    'Família → Buscar → Buscar Família',
                    'Família → Buscar → Família com Indicação RL',
                    'Família → Visualizar Família → Visualizar Histórico Família',
                    'Família → Visualizar Família → Visualizar Histórico Pessoa',
                    'Família → Visualizar Família → Consultar Pessoas Transferidas',
                    'Família → Visualizar Família → Painel Família',
                    'Família → Visualizar Família → Consulta renda integração CNIS',
                    'Família → Visualizar Família → Baixar Formulários',
                    'Consultas → Consulta Qualificação',
                    'Consultas → Consulta de Renda (CNIS)',
                    'Consultas → Escolaridade (Sistema Presença)',
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Família → Visualizar Família → Emissão Comprovante Cadastro',
                    'Questionários → Consultar/Visualizar Qualificação 2024',
                    'Questionários → Consultar/Visualizar Qualificação 2025'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_PROGRAMAS_USUARIOS': {
                'gerais': [
                    'Família → Buscar → Buscar Família',
                    'Família → Buscar → Família com Indicação RL',
                    'Família → Visualizar Família → Visualizar Histórico Família',
                    'Família → Visualizar Família → Visualizar Histórico Pessoa',
                    'Família → Visualizar Família → Consultar Pessoas Transferidas',
                    'Família → Visualizar Família → Painel Família',
                    'Família → Visualizar Família → Baixar Formulários',
                    'Consultas → Consulta Qualificação',
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Família → Visualizar Família → Emissão Folha Resumo',
                    'Questionários → Consultar/Visualizar Qualificação 2024',
                    'Questionários → Consultar/Visualizar Qualificação 2025'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_ORGAOS_CONTROLE': {
                'gerais': [
                    'Família → Buscar → Buscar Família',
                    'Família → Buscar → Família com Indicação RL',
                    'Família → Visualizar Família → Visualizar Histórico Família',
                    'Família → Visualizar Família → Visualizar Histórico Pessoa',
                    'Família → Visualizar Família → Consultar Pessoas Transferidas',
                    'Família → Visualizar Família → Painel Família',
                    'Família → Visualizar Família → Consulta renda integração CNIS',
                    'Família → Visualizar Família → Baixar Formulários',
                    'Consultas → Consulta Qualificação',
                    'Consultas → Consulta de Renda (CNIS)',
                    'Consultas → Escolaridade (Sistema Presença)',
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Família → Visualizar Família → Emissão Folha Resumo',
                    'Questionários → Consultar/Visualizar Qualificação 2024',
                    'Questionários → Consultar/Visualizar Qualificação 2025'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_TRANSMISSAO_FORMULARIO': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Entrevistas Offline → Transmissão Entrevistas Offline (requer PERFIL_USUARIO_COMUM ou PERFIL_GESTOR)'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_ADMINISTRADOR_MD': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral',
                    'Administração do Sistema → Consultar Integrações',
                    'Administração do Sistema → Agendamento de Indisponibilidade',
                    'Administração do Sistema → Bloqueio de Usuários',
                    'Administração do Sistema → Consultar Entrevistas Offline',
                    'Administração do Sistema → Programas Sociais',
                    'Exclusão de Famílias em Lote → Solicitar Exclusões',
                    'Exclusão de Famílias em Lote → Consultar Solicitações'
                ],
                'municipal': [],
                'estadual': [],
                'federal': []
            },
            'PERFIL_ADMINISTRADOR_DTP': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral',
                    'Administração do Sistema → Parâmetros Gerais',
                    'Administração do Sistema → Consultar Integrações',
                    'Administração do Sistema → Agendamento de Indisponibilidade',
                    'Administração do Sistema → Consultar Entrevistas Offline',
                    'Exclusão de Famílias em Lote → Solicitar Exclusões',
                    'Exclusão de Famílias em Lote → Consultar Solicitações'
                ],
                'municipal': [],
                'estadual': [],
                'federal': []
            },
            'PERFIL_ACESSO_MONITORAMENTO': {
                'gerais': [
                    'Mural de Comunicação → Visão geral',
                    'Painéis → Painel Monitoramento'
                ],
                'municipal': [],
                'estadual': [],
                'federal': []
            },
            'PERFIL_CONTESTACAO_INTEGRACAO': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Família → Continuar Inclusão/Alterar Família → Contestar Integração Documentos (requer PERFIL_USUARIO_COMUM ou PERFIL_GESTOR)'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_CARTEIRA_DOCUMENTOS': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral'
                ],
                'municipal': [
                    'Família → Continuar Inclusão/Alterar Família → Alterar Carteira de Documentos (requer PERFIL_USUARIO_COMUM ou PERFIL_GESTOR)'
                ],
                'estadual': [],
                'federal': []
            },
            'PERFIL_ADMINISTRADOR_MURAL': {
                'gerais': [
                    'Mural de Comunicação → Visão Geral',
                    'Mural de Comunicação → Incluir/Alterar/Excluir: Comunicado',
                    'Mural de Comunicação → Incluir/Alterar/Excluir: Evento',
                    'Mural de Comunicação → Incluir/Alterar/Excluir: Informe',
                    'Mural de Comunicação → Incluir/Alterar/Excluir: Tutorial'
                ],
                'municipal': [],
                'estadual': [],
                'federal': []
            }
        }
        self.blocos = {
            'BLOCO1': {
                'campos': [
                    '1.07 - Modalidade da operação',
                    '1.08 - Forma de coleta de dados',
                    '1.09 - Formulários preenchidos',
                    '1.10 - Data da entrevista',
                    '1.11 - Localidade',
                    '1.12 - Tipo de logradouro',
                    '1.13 - Titulo do logradouro',
                    '1.14 - Nome do logradouro',
                    '1.15 - Número do logradouro (obrigatório se 1.16 não for informado)',
                    '1.16 - Complemento do logradouro (obrigatório se 1.15 não for informado)',
                    '1.18 - CEP',
                    '1.19 - Unidade Territorial Local (se estiver habilitado para o município)',
                    '1.21 - Nome do entrevistador',
                    '1.22 - CPF do entrevistador'
                ],
                'criticascruzadas': []
            },
            'BLOCO2': {
                'campos': [
                    '2.01 - O local onde está situado o seu domicílio tem, na maioria, características',
                    '2.02 - Qual a espécie do seu domicílio?',
                    '2.03 - Quantos cômodos tem seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.04 - Quantos cômodos estão servindo, permanentemente, de dormitório para os moradores do seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.05 - Qual é o material predominante no piso do seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.06 - Qual é o material predominante na construção das paredes externas do seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.07 - O seu domicílio tem água canalizada para, pelo menos, um cômodo? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.08 - Qual é a forma de abastecimento de água utilizada no seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.09 - No seu domicílio ou na propriedade existe banheiro ou sanitário? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.10 - De que forma é feito o escoamento do banheiro ou sanitário? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.11 - O lixo do seu domicílio: (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.12 - Qual é a forma de iluminação utilizada no seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)',
                    '2.13 - Existe calçamento/pavimentação no trecho do logradouro (rua, avenida, etc.), em frente ao seu domicílio? (Será obrigatório se 2.02 for 1 - Particular Permanente)'
                ],
                'criticascruzadas': [
                    'Caso o campo 1.09 tiver marcado a opção 4 - Pessoa em situação de rua(FS2) esse bloco estará indisponível',
                    'Caso o campo 2.07 tiver marcado Não o campo 2.08 ficará desabilitado',
                    'Caso o campo 2.09 tiver marcado Não o campo 2.10 ficará desabilitado'
                ]
            },
            'BLOCO3': {
                'campos': [
                    '3.01 - A Família é indígena?',
                    '3.02 - A que povo indígena pertence a família? (Será obrigatório se marcado o campo 3.01 como Sim)',
                    '3.03 - A família reside em terra ou reserva indígena? (Será obrigatório se marcado o campo 3.01 como Sim)',
                    '3.04 - Qual é o nome da terra ou reserva indígena? (Será obrigatório se marcado o campo 3.03 como Sim)',
                    '3.05 - A família é quilombola?',
                    '3.06 - Qual é o nome da comunidade quilombola? (Será obrigatório se marcado o campo 3.05 como Sim)',
                    '3.07 - Quantas pessoas moram no seu domicílio?',
                    '3.08 - Quantas famílias moram no seu domicílio?',
                    '3.09 - Há alguma pessoa dessa família internada, abrigada ou privada de liberdade há 12 meses ou mais?',
                    '3.09.1 - Criança(s) e adolescente(s) (de 0 a 17 anos) (Pode marcar a opção 0 - Não tem)',
                    '3.09.2 - Jovem(ns) e adulto(s) (de 18 a 59 anos) (Pode marcar a opção 0 - Não tem)',
                    '3.09.3 - Idoso(s) (de 60 anos ou mais) (Pode marcar a opção 0 - Não tem)',
                    '3.10 - A família, normalmente, tem despesa mensal com:',
                    '3.10.1 - Energia elétrica (Pode marcar a opção 0 - Não tem)',
                    '3.10.2 - Água e esgoto (Pode marcar a opção 0 - Não tem)',
                    '3.10.3 - Gás, carvão e lenha (Pode marcar a opção 0 - Não tem)',
                    '3.10.4 - Alimentação, higiene e limpeza (Pode marcar a opção 0 - Não tem)',
                    '3.10.5 - Transporte (Pode marcar a opção 0 - Não tem)',
                    '3.10.6 - Aluguel (Pode marcar a opção 0 - Não tem)',
                    '3.10.7 - Medicamentos de uso regular (Pode marcar a opção 0 - Não tem)',
                    '3.11 - Código e nome do Estabelecimento de Assistência à Saúde - EAS/MS em que os integrantes da família são atendidos quando necessitam',
                    '3.12 - Código e nome do Centro da Assistência Social (CRAS/CREAS) em que os integrantes da família são atendidos quando necessitam',
                    '3.13 - Família identificada em situação de risco social associado à violação de direitos',
                    '3.14 - Família em risco para insegurança alimentar'
                ],
                'criticascruzadas': [
                    'O campo 3.07 será obrigatório se o campo 2.02 for marcado como 1- Particular Permanente',
                    'O campo 3.08 será obrigatório se o campo 2.02 for marcado como 1- Particular Permanente',
                ]
            },
            'BLOCO4': {
                'campos': [
                    '4.01 - Número de ordem',
                    '4.02 - Nome completo',
                    '4.03 - Identificação (NIS/PIS/PASEP)',
                    '4.04 - Nome social (Será obrigatório se o campo 4.16 for marcado como 1 - Sim e a opção 4.17 for diferente de Não e a pessoa pedir para informar o campo)',
                    '4.05 - Sexo',
                    '4.06 - Data de nascimento',
                    '4.07 - Relação de parentesco de <nome> com a pessoa Responsável pela Unidade Familiar - RF (será obrigatório se a família não for RL)',
                    '4.08 - Cor ou raça',
                    '4.09 - Filiação 1 (ou nome completo da mãe) (Pode marcar a opção 2 - Não sabe)',
                    '4.10 - Filiação 2 (Pode marcar a opção 2 - Não sabe)',
                    '4.11 - Onde <nome> nasceu?',
                    '4.12 - Em que estado <nome> nasceu? (Pode marcar a opção 2 - Não sabe)',
                    '4.13 - Em que município <nome> nasceu? (Pode marcar a opção 2 - Não sabe)',
                    '4.14 - Em que país estrangeiro <nome> nasceu? (Pode marcar a opção 2 - Não sabe)',
                    '4.15- O nascimento de <nome> foi registrado em Cartório de Registro Civil?',
                    '4.16- Deseja informar o gênero de <nome>?',
                    '4.17- <nome> é pessoa trans ou travesti? (Será obrigatório se o campo 4.16 for marcado como 1 - Sim)',
                    '4.18- Qual é o gênero/identidade de gênero de <nome>? (Será obrigatório se o campo 4.16 for marcado como 1 - Sim)',
                ],
                'criticascruzadas': [
                    
                ]
            },
            'BLOCO5': {
                'campos': [
                    '5.01 - Tipo e dados da certidão',
                    '5.01.a - Tipo',
                    '5.01.b - Dados',
                    '5.01.b.1 - Nome do cartório',
                    '5.01.b.2 - Data do registro',
                    '5.01.b.3 - Número do livro',
                    '5.01.b.4 - Número da folha',
                    '5.01.b.5 - Número do termo/RANI',
                    '5.01.b.6 - Matrícula',
                    '5.01.b.7 - Estado de registro',
                    '5.01.b.8 - Município de registro',
                    '5.02 - Número de inscrição do CPF',
                    '5.03 - Dados do documento de identidade (RG)',
                    '5.03.1 - Número',
                    '5.03.2 - Complemento',
                    '5.03.3 - Data da emissão',
                    '5.03.4 - Estado emissor',
                    '5.03.5 - Sigla do órgão emissor',
                    '5.04 - Dados da Carteira de Trabalho e Previdência Social',
                    '5.04.1 - Número',
                    '5.04.2 - Série',
                    '5.04.3 - Data da emissão',
                    '5.04.4 - Estado emissor',
                    '5.05 - Dados do título de eleitor com DV',
                    '5.05.1 - Número',
                    '5.05.2 - Zona',
                    '5.05.3 - Seção'
                ],
                'criticascruzadas': [
                    'Caso o campo 4.15 for marcado como 3 - Não ou 4 - Não sabe o bloco ficará desabilitado'
                ]
            },
            'BLOCO6': {
                'campos': [
                    '6.01 - <nome> tem alguma deficiência permanente que limite as suas atividades habituais (como trabalhar, ir à escola, brincar, etc.)',
                    '6.02 - Qual(is Qual é o tipo de deficiência que <nome> tem? (Este quesito admite múltipla marcação) (Será obrigatório se o campo 6.01 for marcado com 1 - Sim)',
                    '6.03 - Em função dessa deficiência <nome> recebe cuidados permanentes de terceiros ? (Este quesito admite múltipla marcação) (Será obrigatório se o campo 6.01 for marcado com 1 - Sim)'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCO7': {
                'campos': [
                    '7.01 - <nome> sabe ler e escrever?',
                    '7.02 - <nome> frequenta escola ou creche?',
                    '7.03 - Qual é o nome dessa escola ou creche que <nome> frequenta?',
                    '7.04 - Esta escola ou creche está localizada neste município?',
                    '7.05 - Qual é o estado e o município onde está localizada a escola ou creche?',
                    '7.05.1 - Estado',
                    '7.05.2 - Município',
                    '7.06 - Código do INEP/MEC da escola ou creche',
                    '7.07 - Qual é o curso que <nome> frequenta',
                    '7.08 - Qual é o ano/série que <nome> frequenta?',
                    '7.09 - Qual foi o curso mais elevado que <nome> frequentou, no qual concluiu pelo menos uma série?',
                    '7.10 - Qual foi o último ano/série que <nome> concluiu com aprovação nesse curso que frequentou?',
                    '7.11 - DOMINGOS concluiu esse curso que frequentou?'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCO8': {
                'campos': [
                    '8.01 - Na semana passada DOMINGOS trabalhou?',
                    '8.02 - Na semana passada DOMINGOS estava afastado de um trabalho, por motivo de doença, falta voluntária, licença, férias ou por outro motivo?',
                    '8.03 - Esse trabalho principal que DOMINGOS exerceu foi na agricultura, criação de animais, pesca ou coleta (extração vegetal)?',
                    '8.04 - Nesse trabalho principal DOMINGOS era:',
                    '8.05 - No mês passado DOMINGOS recebeu remuneração de trabalho? (Se sim, registre o valor bruto da remuneração efetivamente recebida em todos os trabalhos)',
                    '8.06 - DOMINGOS teve trabalho remunerado nos últimos 12 meses?',
                    '8.07 - Quantos meses trabalhou nesse período?',
                    '8.08 - Qual foi a remuneração bruta de todos os trabalhos recebidos por DOMINGOS nesse período?',
                    '8.09 - Quanto DOMINGOS recebe, normalmente, por mês de:',
                    '8.09.1 - Ajuda/doação regular de não morador',
                    '8.09.2 - Aposentadoria, aposentadoria rural, pensão ou BPC/LOAS',
                    '8.09.3 - Seguro-desemprego',
                    '8.09.4 - Pensão alimentícia',
                    '8.09.5 - Outras fontes de remuneração exceto bolsa família ou outras transferências similares'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCOFS2': {
                'campos': [
                    '',
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCO9': {
                'campos': [
                    '9.01 - Contato(s)',
                    '9.01.a - Telefone primário - Tipo',
                    '9.01.a - Telefone primário - DDD',
                    '9.01.a - Telefone primário - Número',
                    '9.01.a - Telefone primário - Autoriza recebimento de mensagem',
                    '9.01.a - Telefone secundário - Tipo',
                    '9.01.a - Telefone secundário - DDD',
                    '9.01.a - Telefone secundário - Número',
                    '9.01.a - Telefone secundário - Autoriza recebimento de mensagem',
                    '9.01.c - Email - Tipo',
                    '9.01.c - Email - Email',
                    '9.01.c - Email - Autoriza recebimento de E-mail',
                    '9.02 - Documentos'
                    '9.02 - Documentos - Documento Unipessoal'
                    '9.02 - Documentos - Declaração Unipessoal'
                    '9.02 - Documentos - Autorização'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCO10': {
                'campos': [
                    '10.01 - Há trabalho infantil na família?',
                    '10.02 - Identifique a(s) criança(s) envolvida(s) em trabalho infantil'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCOFS1': {
                'campos': [
                    '2.01 -Indique abaixo, marcando com X, se a família ou algum integrante da família é beneficiário de algum programa da Secretaria Nacional de Segurança Alimentar e Nutricional - SESAN.',
                    '2.02 - Algum integrante da família foi resgatado do trabalho análogo ao de escravo por órgão do governo (Ministério do Trabalho, Polícia Federal, etc.)?',
                    '2.03 -Indique abaixo, marcando com X, se a família ou algum integrante da família é beneficiário de algum programa do Ministério de Minas e Energia.',
                    '2.04 - Preencha o campo abaixo com o número/código da unidade consumidora, indicado na conta de energia elétrica do domicílio',
                    '2.04.a - Nº de ordem da pessoa',
                    '2.04.b - Código da unidade consumidora',
                    '2.05 -Indique abaixo, marcando com X, se algum integrante da família recebe algum benefício ou é atendido por algum programa da Assistência Social',
                    '2.07 - Sua família pertence a algum Grupo Populacional Tradicional ou Específico?'
                ],
                'criticascruzadas': [
                ]
            },
            'BLOCOFS3': {
                'campos': [
                    '3.01 - Nome completo',
                    '3.02 - Identificação (NIS)',
                    '3.03 - Sexo',
                    '3.04 - Data de nascimento',
                    '3.05 - Filiação 1 (ou nome completo da mãe)',
                    '3.06 - Filiação 2',
                    '3.07 - CPF',
                    '3.08 - Onde AEMILI nasceu?',
                    '3.09 - Em que estado AEMILI nasceu?',
                    '3.10 - Em que município AEMILI nasceu?',
                    '3.11 - Em que país estrangeiro AEMILI nasceu?',
                    '3.12 - Telefones de contato',
                    '3.12.a - DDD',
                    '3.12.b - Telefone 1',
                    '3.12.c - DDD',
                    '3.12.d - Telefone 2',
                    '3.13 - E-mail',
                    '3.14 - Tipo de representação legal',
                    '3.15 - Informações de documento do representante legal',
                    '3.16 - Localidade',
                    '3.17 - UF',
                    '3.18 - Município',
                    '3.19 - Tipo',
                    '3.20 - Nome',
                    '3.21 - Número',
                    '3.22 - Complemento do número',
                    '3.23 - CEP'
                ],
                'criticascruzadas': [
                ]
            }
        }

    def consultar_funcionalidades(self, perfil, abrangencia):
        """
        Consulta as funcionalidades disponíveis para um perfil em uma abrangência específica
        
        Args:
            perfil (str): Nome do perfil de acesso
            abrangencia (str): Abrangência (municipal, estadual, federal)
        
        Returns:
            dict: Dicionário com as funcionalidades disponíveis
        """
        perfil = perfil.upper()
        abrangencia = abrangencia.lower()
        
        if perfil not in self.perfis:
            return {"erro": f"Perfil '{perfil}' não encontrado"}
        
        if abrangencia not in ['municipal', 'estadual', 'federal']:
            return {"erro": f"Abrangência '{abrangencia}' inválida. Use: municipal, estadual ou federal"}
        
        funcionalidades_gerais = self.perfis[perfil]['gerais']
        funcionalidades_especificas = self.perfis[perfil][abrangencia]
        
        return {
            "perfil": perfil,
            "abrangencia": abrangencia.title(),
            "funcionalidades_gerais": funcionalidades_gerais,
            "funcionalidades_especificas": funcionalidades_especificas,
            "total_funcionalidades": len(funcionalidades_gerais) + len(funcionalidades_especificas)
        }

    def consultar_bloco(self, bloco):
        """
        Consulta as funcionalidades disponíveis para um bloco
        
        Args:
            bloco (str): Nome do bloco
        
        Returns:
            dict: Dicionário com os campos
        """
        bloco = bloco.upper()
        
        if bloco not in self.blocos:
            return {"erro": f"Bloco '{bloco}' não encontrado"}
        
        campo = self.blocos[bloco]['campos']
        criticascruzadas = self.blocos[bloco]['criticascruzadas']

        return {
            "bloco": bloco,
            "campos": campo,
            "criticascruzadas": criticascruzadas
        }

    def listar_perfis(self):
        """Lista todos os perfis disponíveis"""
        return list(self.perfis.keys())

    def listar_abrangencias(self):
        """Lista todas as abrangências disponíveis"""
        primeiro_perfil = next(iter(self.perfis.values()))
        return [k for k in primeiro_perfil.keys() if k != 'gerais']

    def adicionar_perfil(self, nome_perfil):
        nome_perfil = nome_perfil.upper()
        if nome_perfil in self.perfis:
            return {"erro": f"Perfil '{nome_perfil}' já existe"}
        abrangencias = {ab: [] for ab in self.listar_abrangencias()}
        self.perfis[nome_perfil] = {'gerais': [], **abrangencias}
        return {"sucesso": f"Perfil '{nome_perfil}' criado"}

    def adicionar_abrangencia(self, nome_abrangencia):
        nome_abrangencia = nome_abrangencia.lower()
        if nome_abrangencia in self.listar_abrangencias():
            return {"erro": f"Abrangência '{nome_abrangencia}' já existe"}
        for perfil in self.perfis.values():
            perfil[nome_abrangencia] = []
        return {"sucesso": f"Abrangência '{nome_abrangencia}' adicionada a todos os perfis"}

    def adicionar_funcionalidade(self, perfil, abrangencia, funcionalidade):
        perfil = perfil.upper()
        abrangencia = abrangencia.lower()
        if perfil not in self.perfis:
            return {"erro": f"Perfil '{perfil}' não encontrado"}
        chave = 'gerais' if abrangencia == 'gerais' else abrangencia
        if chave not in self.perfis[perfil]:
            return {"erro": f"Abrangência '{abrangencia}' não encontrada"}
        if funcionalidade in self.perfis[perfil][chave]:
            return {"erro": f"Funcionalidade já existe neste perfil/abrangência"}
        self.perfis[perfil][chave].append(funcionalidade)
        return {"sucesso": f"Funcionalidade adicionada em {perfil} → {chave}"}

    def remover_funcionalidade(self, perfil, abrangencia, funcionalidade):
        perfil = perfil.upper()
        abrangencia = abrangencia.lower()
        if perfil not in self.perfis:
            return {"erro": f"Perfil '{perfil}' não encontrado"}
        chave = 'gerais' if abrangencia == 'gerais' else abrangencia
        if chave not in self.perfis[perfil]:
            return {"erro": f"Abrangência '{abrangencia}' não encontrada"}
        if funcionalidade not in self.perfis[perfil][chave]:
            return {"erro": f"Funcionalidade não encontrada neste perfil/abrangência"}
        self.perfis[perfil][chave].remove(funcionalidade)
        return {"sucesso": f"Funcionalidade removida de {perfil} → {chave}"}

    def remover_perfil(self, nome_perfil):
        nome_perfil = nome_perfil.upper()
        if nome_perfil not in self.perfis:
            return {"erro": f"Perfil '{nome_perfil}' não encontrado"}
        del self.perfis[nome_perfil]
        return {"sucesso": f"Perfil '{nome_perfil}' removido"}

    def listar_blocos(self):
        """Lista todos os blocos disponíveis"""
        return list(self.blocos.keys())

def _selecionar_perfil(sistema):
    """Solicita seleção de perfil ao usuário"""
    print("Perfis disponíveis:")
    for i, perfil in enumerate(sistema.listar_perfis(), 1):
        print(f"{i}. {perfil}")
    entrada = input("\nPerfil (número ou nome): ").strip()
    if entrada.isdigit():
        idx = int(entrada) - 1
        perfis = sistema.listar_perfis()
        return perfis[idx] if 0 <= idx < len(perfis) else None
    return entrada

def _selecionar_abrangencia(sistema, incluir_gerais=False):
    """Solicita seleção de abrangência ao usuário"""
    abrangencias = sistema.listar_abrangencias()
    if incluir_gerais:
        abrangencias = ['gerais'] + abrangencias
    print("\nAbrangências disponíveis:")
    for i, ab in enumerate(abrangencias, 1):
        print(f"{i}. {ab.title()}")
    entrada = input("\nAbrangência (número ou nome): ").strip()
    if entrada.isdigit():
        idx = int(entrada) - 1
        return abrangencias[idx] if 0 <= idx < len(abrangencias) else None
    return entrada

def _menu_consultar(sistema):
    perfil = _selecionar_perfil(sistema)
    if not perfil:
        print("Perfil inválido!"); return
    abrangencia = _selecionar_abrangencia(sistema)
    if not abrangencia:
        print("Abrangência inválida!"); return
    resultado = sistema.consultar_funcionalidades(perfil, abrangencia)
    print("\n" + "="*80)
    if "erro" in resultado:
        print(f"ERRO: {resultado['erro']}")
    else:
        print(f"PERFIL: {resultado['perfil']}")
        print(f"ABRANGÊNCIA: {resultado['abrangencia']}")
        print(f"TOTAL DE FUNCIONALIDADES: {resultado['total_funcionalidades']}")
        print(f"\nFUNCIONALIDADES GERAIS ({len(resultado['funcionalidades_gerais'])}):")
        for func in resultado['funcionalidades_gerais']:
            print(f"  • {func}")
        if resultado['funcionalidades_especificas']:
            print(f"\nFUNCIONALIDADES ESPECÍFICAS - {resultado['abrangencia'].upper()} ({len(resultado['funcionalidades_especificas'])}):")
            for func in resultado['funcionalidades_especificas']:
                print(f"  • {func}")
        else:
            print(f"\nNenhuma funcionalidade específica para abrangência {resultado['abrangencia']}")
    print("="*80)

def _menu_adicionar_perfil(sistema):
    nome = input("Nome do novo perfil: ").strip()
    resultado = sistema.adicionar_perfil(nome)
    print(resultado.get("sucesso") or f"ERRO: {resultado['erro']}")

def _menu_adicionar_abrangencia(sistema):
    nome = input("Nome da nova abrangência: ").strip()
    resultado = sistema.adicionar_abrangencia(nome)
    print(resultado.get("sucesso") or f"ERRO: {resultado['erro']}")

def _menu_adicionar_funcionalidade(sistema):
    perfil = _selecionar_perfil(sistema)
    if not perfil:
        print("Perfil inválido!"); return
    abrangencia = _selecionar_abrangencia(sistema, incluir_gerais=True)
    if not abrangencia:
        print("Abrangência inválida!"); return
    funcionalidade = input("Funcionalidade (ex: Categoria → Subcategoria → Ação): ").strip()
    resultado = sistema.adicionar_funcionalidade(perfil, abrangencia, funcionalidade)
    print(resultado.get("sucesso") or f"ERRO: {resultado['erro']}")

def _menu_remover_perfil(sistema):
    perfil = _selecionar_perfil(sistema)
    if not perfil:
        print("Perfil inválido!"); return
    confirma = input(f"Confirma remoção do perfil '{perfil.upper()}'? (s/n): ").strip().lower()
    if confirma == 's':
        resultado = sistema.remover_perfil(perfil)
        print(resultado.get("sucesso") or f"ERRO: {resultado['erro']}")
    else:
        print("Operação cancelada.")

def _menu_remover_funcionalidade(sistema):
    perfil = _selecionar_perfil(sistema)
    if not perfil:
        print("Perfil inválido!"); return
    abrangencia = _selecionar_abrangencia(sistema, incluir_gerais=True)
    if not abrangencia:
        print("Abrangência inválida!"); return
    chave = 'gerais' if abrangencia.lower() == 'gerais' else abrangencia.lower()
    perfil_upper = perfil.upper()
    if perfil_upper not in sistema.perfis or chave not in sistema.perfis[perfil_upper]:
        print("Perfil ou abrangência não encontrado!"); return
    funcs = sistema.perfis[perfil_upper][chave]
    if not funcs:
        print("Nenhuma funcionalidade para remover."); return
    print("\nFuncionalidades:")
    for i, f in enumerate(funcs, 1):
        print(f"{i}. {f}")
    entrada = input("\nNúmero da funcionalidade a remover: ").strip()
    if entrada.isdigit() and 0 < int(entrada) <= len(funcs):
        resultado = sistema.remover_funcionalidade(perfil, abrangencia, funcs[int(entrada) - 1])
        print(resultado.get("sucesso") or f"ERRO: {resultado['erro']}")
    else:
        print("Seleção inválida!")

def main():
    sistema = SistemaPerfilAcesso()
    
    opcoes = {
        '1': ('Consultar funcionalidades', _menu_consultar),
        '2': ('Adicionar perfil', _menu_adicionar_perfil),
        '3': ('Adicionar abrangência', _menu_adicionar_abrangencia),
        '4': ('Adicionar funcionalidade', _menu_adicionar_funcionalidade),
        '5': ('Remover funcionalidade', _menu_remover_funcionalidade),
        '6': ('Remover perfil', _menu_remover_perfil),
        '0': ('Sair', None)
    }
    
    while True:
        print("\n=== Sistema de Perfis de Acesso ===")
        for k, (desc, _) in opcoes.items():
            print(f"{k}. {desc}")
        
        escolha = input("\nOpção: ").strip()
        
        if escolha == '0':
            break
        if escolha in opcoes and opcoes[escolha][1]:
            print()
            opcoes[escolha][1](sistema)
            input("\nPressione Enter para continuar...")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
