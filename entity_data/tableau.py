import numpy as np
import json


class TableauData:
    def __init__(self,idEntity,datas):

        self.idEntity = idEntity
        self.data_2022 = np.array(self.adapt_array(datas["data_2022"]))
        self.validation_2022 = np.array(self.adapt_array(datas["validation_2022"]))

        self.data_2023 = np.array(self.adapt_array(datas["data_2021"]))
        self.validation_2023 = np.array(self.adapt_array(datas["validation_2021"]))


    def dataToAppWrite(self):
        return {
            "data_2022":self.data_2022.tolist(),
            "validation_2022": self.validation_2022.tolist(),
            "data_2021": self.data_2023.tolist(),
            "validation_2021": self.validation_2023.tolist(),
        }

    def getDataJson(self):
        return {
            "data_2022": self.data_2022,
            "validation_2022": self.validation_2022,
            "data_2021": self.data_2023,
            "validation_2021": self.validation_2023,
        }

    def dataToFlutter(self):
        return {
            "data_2022":self.data_2022.transpose().tolist(),
            "validation_2022": self.validation_2022.transpose().tolist(),
            "data_2021": self.data_2023.transpose().tolist(),
            "validation_2021": self.validation_2023.transpose().tolist(),
        }

    def updateCellData(self,value,rowId,moisId,annee):
        dataJson = self.getDataJson()
        dataYear = dataJson['data_'+str(annee)]
        dataYear[rowId][moisId+1] = value
        self.calculMensuel(dataYear)
        self.calculRealiseAnnuel(dataYear)
        #dataYear[2][10] = dataYear[0][10] +dataYear[1][10]
        return dataYear

    def filterSum(self,list):
        list2 = []
        for l in list:
            if l is not None:
                list2.append(l)
        return list2

    def calculMensuel(self,dataYear):
        index = 1
        for i in range(1,13):
            # GEN-003 : GEN-001+GEN-003
            list = self.filterSum([dataYear[1-index][i],dataYear[2-index][i]])
            if len(list) > 0 :
                dataYear[3-index][i] = sum(list)
            # GOU1b-003

    def calculRealiseAnnuel(self,dataYear):
        index = 1
        for i in range(60):
            list = self.filterSum(dataYear[i][1:])
            if len(list) > 0:
                dataYear[i][0] = sum(list)

    def validateCellData(self,value,rowId,moisId,annee):
        dataJson = self.getDataJson()
        validatedDataYear = dataJson['validation_'+str(annee)]
        validatedDataYear[rowId][moisId+1] = value
        return validatedDataYear

    def adapt_string(self):

        datas = self.dataToAppWrite()
        json_encoded_list = json.dumps(datas)
        return json_encoded_list

    def adapt_array(self,jsonString):

        return json.loads(jsonString)
