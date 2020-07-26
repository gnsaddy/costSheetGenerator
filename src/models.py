from django.utils.timezone import datetime
from django.db import models
from django.contrib.auth.models import User

t = (
    ('', 'Choose..'),
    ('mr', 'Merchant'),
    ('vd', 'Vendor')
)


class UserProfile(models.Model):
    holder = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    mobile = models.IntegerField()
    userType = models.CharField(max_length=100, choices=t)

    def __str__(self):
        return self.holder.first_name + " " + self.holder.last_name


class CostSheetName(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    costSheetName = models.CharField(max_length=100, null=True)
    buyer = models.CharField(max_length=100, null=True)
    styleNum = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    season = models.CharField(max_length=100, null=True)
    order_quant = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    createdDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.costSheetName + " -- " + str(self.createdDate.date())


class Embroidery(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    embroideryDes = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    consumption = models.CharField(max_length=100, null=True)
    extraAllowance = models.CharField(max_length=100, null=True)
    rate = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.embroideryDes


class Fabric(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    fabricName = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100, null=True)
    gsm = models.CharField(max_length=100, null=True)
    yarnCount = models.CharField(max_length=100, null=True)
    construction = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    consumption = models.CharField(max_length=100, null=True)
    totalWidth = models.CharField(max_length=100, null=True)
    extraAllowance = models.CharField(max_length=100, null=True)
    rate = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    importDuty = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.fabricName


class Thread(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    threadType = models.CharField(max_length=100, null=True)
    threadColor = models.CharField(max_length=100, null=True)
    consumption = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100, null=True)
    tktSize = models.CharField(max_length=100, null=True)
    cost_unit = models.CharField(max_length=100, null=True)
    extraAllowance = models.CharField(max_length=100, null=True)
    importDuty = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.threadType


class MainLabel(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    labelType = models.CharField(max_length=100, null=True)
    textType = models.CharField(max_length=100, null=True)
    dimension = models.CharField(max_length=100, null=True)
    rate = models.CharField(max_length=100, null=True)
    extraAllowance = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    importDuty = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.labelType


class PolyBag(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    polyBagType = models.CharField(max_length=100, null=True)
    polyBagMaterial = models.CharField(max_length=100, null=True)
    dimension = models.CharField(max_length=100, null=True)
    cost_unit = models.CharField(max_length=100, null=True)
    extraAllowance = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    importDuty = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.polyBagType


class CMT(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    related = models.ForeignKey(CostSheetName, on_delete=models.CASCADE, null=True, default=None)
    cmtCost = models.CharField(max_length=100, null=True)
    packagingCharge = models.CharField(max_length=100, null=True)
    factoryOverheadCost = models.CharField(max_length=100, null=True)
    testingCost = models.CharField(max_length=100, null=True)
    otherCost = models.CharField(max_length=100, null=True)
    logisticCost = models.CharField(max_length=100, null=True)
    factoryMarkup = models.CharField(max_length=100, null=True)
    totalInr = models.CharField(max_length=100, null=True)
    agentMarkup = models.CharField(max_length=100, null=True)
    factoryFOB = models.CharField(max_length=100, null=True)
    clientFOB = models.CharField(max_length=100, null=True)
    constractualCost = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.holder.first_name + " -- " + self.cmtCost
