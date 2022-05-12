from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class ChequePrintTemplate(models.Model):
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    starting_position_from_top_edge = models.FloatField()
    cheque_width = models.FloatField()
    cheque_height = models.FloatField()
    acc_pay_dist_from_top_edge = models.FloatField()
    acc_pay_dist_from_left_edge = models.FloatField()
    message_to_show = models.FloatField()
    date_dist_from_top_edge = models.FloatField()
    date_dist_from_left_edge = models.FloatField()
    payer_name_from_top_edge = models.FloatField()
    payer_name_from_left_edge = models.FloatField()
    amt_in_words_from_top_edge = models.FloatField()
    amt_in_words_from_left_edge = models.FloatField()
    amt_in_word_width = models.FloatField()
    amt_in_words_line_spacing = models.FloatField()
    amt_in_figures_from_top_edge = models.FloatField()
    amt_in_figures_from_left_edge = models.FloatField()
    acc_no_dist_from_top_edge = models.FloatField()
    acc_no_dist_from_left_edge = models.FloatField()
    signatory_from_top_edge = models.FloatField()
    signatory_from_left_edge = models.FloatField()
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='chart_of_accounts_importer_modified_by')

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name_plural = "Cheque_Print_Templates"



