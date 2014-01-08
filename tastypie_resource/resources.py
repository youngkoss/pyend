from tastypie.resources import ModelResource


class ModelResource(ModelResource):

    def determine_format(self, request):
        return 'application/json'
