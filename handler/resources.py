from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resource_dict(self, row):
        result = {}
        result['resID'] = row[0]
        result['resName'] = row[1]
        result['catID'] = row[2]
        result['resSpecifications'] = row[3]
        return result

    def build_resource_attributes(self, resID, resName, catID, resSpecifications):
        result = {}
        result['resID'] = resID
        result['resName'] = resName
        result['catID'] = catID
        result['resSpecifications'] = resSpecifications
        return result

    def build_cat_dict(self, row):
        result = {}
        result['resName'] = row[0]
        result['resSpecifications'] = row[1]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, resID):
        dao = ResourcesDAO()
        row = dao.getResourceById(resID)
        if not row:
            return jsonify(Error="Resource not found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def getResourcesByCity(self, city):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByCity(city)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllAvailableResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllAvailableResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(AvailableResources = result_list)

    def getResourcesByCategoryName(self, catName):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByCategoryName(catName)
        result_list = []
        for row in resources_list:
            result = self.build_cat_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getAvailableResourcesByCategories(self, catName):
        dao = ResourcesDAO()
        resources_list = dao.getAvailableResourcesByCategories(catName)
        result_list = []
        for row in resources_list:
            result = self.build_cat_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResourcesByArguments(self, args):
        dao = ResourcesDAO()
        if not 'orderby' in args:
            resources_list = dao.searchResourcesByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            resources_list = dao.searchResourcesWithSorting(args.get('orderby'))
        else:
            resources_list = dao.searchResourcesByArgumentsWithSorting(args)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def insertResource(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            resName = form['resName']
            catID = form['catID']
            resSpecifications = form['resSpecifications']

            if resName and catID and resSpecifications:
                resDao = ResourcesDAO()
                resID = resDao.insert(resName, catID, resSpecifications)
                result = self.build_resource_attributes(resID, resName, catID, resSpecifications)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400