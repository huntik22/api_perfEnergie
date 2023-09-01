dataEnityJson = {}

annees = [2021,2022,2023]
entitesId = ["palmci","palmci_siege","palmci_ehania","palmci_iboke",
          "sifca_groupe","sifca_holding",
          "sucrivoire","sucrivoire_siege","sucrivoire_zuenoula","sucrivoire_borotou_koro"]

entitesSub = ["palmci","palmci","palmci","palmci",
          "sifca","sifca",
          "sucrivoire","sucrivoire","sucrivoire","sucrivoire"]

entiteName = [ 'PALMCI', 'Palmci Siège', 'Palmci Ehania', 'Palmci Iboké',
               'SIFCA Groupe', 'SIFCA HOLDING',
               'SUCRIVOIRE', 'Sucrivoire Siège','Sucrivoire Zuénoula', 'Sucrivoire Borotou-Koro']

abrEntites =["plmci","plmci_siege","plmci_ehnia","plmci_iboke",
          "sifca_grpe","sifca_holdg",
          "scriv","scriv_siege","scriv_znla","scriv_btkr"]

listPiliers = [
          "1 GOUVERNANCE ET ÉTHIQUE",
          "2 EMPLOI ET CONDITIONS DE TRAVAIL",
          "3 COMMUNAUTES ET INNOVATION SOCIETALE",
          "4 ENVIRONNEMENT"
        ]

listEnjeux = [
          "1a Gouvernance DD et stratégie",
          "1b Pilotage DD",
          "2 Éthique des affaires et achats responsables",
          "3 Intégration des attentes DD des clients et consommateurs",
          "4 Égalité de traitement",
          "5 Conditions de travail",
          "6 Amélioration du cadre de vie",
          "7 Inclusion sociale et développement des communautés",
          "8 Changement climatique et déforestation",
          "9 Gestion et traitement de l’eau",
          "10 Gestion des ressources et déchets"
        ]

listOfIndex = ['GEN-001', 'GEN-002', 'GEN-003', 'GEN-004', 'GEN-005', 'GEN-006', 'GEN-007', 'GEN-008', 'GEN-009', 'GEN-010',
      'GOU1a-001', 'GOU1a-002', 'GOU1a-003', 'GOU1a-004', 'GOU1a-005', 'GOU1a-006', 'GOU1a-007', 'GOU1a-008', 'GOU1b-001',
      'GOU1b-002', 'GOU1b-003', 'GOU1b-004', 'GOU1b-005', 'GOU1b-006', 'GOU1b-007', 'GOU1b-008', 'GOU1b-009', 'GOU1b-010',
      'GOU2-001', 'GOU2-002', 'GOU2-003', 'GOU2-004', 'GOU2-005', 'GOU2-006', 'GOU2-007', 'GOU2-008', 'GOU2-009', 'GOU2-010',
      'GOU3-001', 'GOU3-002', 'GOU3-003', 'GOU3-004', 'GOU3-005', 'GOU3-006', 'GOU3-007', 'GOU3-008', 'GOU3-009',
      'EMP4-001', 'EMP4-002', 'EMP4-003', 'EMP4-004', 'EMP4-005', 'EMP4-006', 'EMP4-007', 'EMP4-008',
      'EMP4-009', 'EMP4-010', 'EMP5-001', 'EMP5-002', 'EMP5-003', 'EMP5-004', 'EMP5-005', 'EMP5-006',
      'EMP5-007', 'EMP5-008', 'EMP5-009', 'EMP5-010', 'EMP6-001', 'EMP6-002', 'EMP6-003', 'EMP6-004',
      'EMP6-005', 'EMP6-006', 'EMP6-007', 'EMP6-008', 'INC7-001', 'INC7-002', 'INC7-003', 'INC7-004',
      'INC7-005', 'INC7-006', 'INC7-007', 'INC7-008', 'INC7-009', 'INC7-010', 'ENV8-001', 'ENV8-002',
      'ENV8-003', 'ENV8-004', 'ENV8-005', 'ENV8-006', 'ENV8-007', 'ENV8-008', 'ENV8-009', 'ENV8-010',
      'ENV9-001', 'ENV9-002', 'ENV9-003', 'ENV9-004', 'ENV9-006', 'ENV9-005', 'ENV9-007', 'ENV9-008',
      'ENV9-009', 'ENV9-010', 'ENV10-001', 'ENV10-002', 'ENV10-003', 'ENV10-004', 'ENV10-005', 'ENV10-006',
      'ENV10-007', 'ENV10-008', 'ENV10-009', 'ENV10-010']

def getNameById(id):
    name = entiteName[entitesId.index(id)]
    return

def getSuiviIdByName(name):
    abr = abrEntites[entiteName.index(name)]
    return abr+"_suivi_"

def getPerfByName(name):
    entity = entitesId[entiteName.index(name)]
    return entity+"_"

def getEntityByName(name):
    entity = entitesId[entiteName.index(name)]
    return entity