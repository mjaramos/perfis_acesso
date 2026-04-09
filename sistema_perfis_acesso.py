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
            'PERFIL_ADMINISTRADOR_MDS': {
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
            'PERFIL_ADMINISTRADOR_DATAPREV': {
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