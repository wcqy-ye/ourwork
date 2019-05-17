from haystack import indexes
# 修改此处，为你自己的model
from loginupin.models import *


# 修改此处，类名为模型类的名称+Index，比如模型类为GoodsInfo,则这里类名为GoodsInfoIndex
class usersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 修改此处，为你自己的model
        return users

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class commentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 修改此处，为你自己的model
        return comment

    def index_queryset(self, using=None):
        return self.get_model().objects.all()