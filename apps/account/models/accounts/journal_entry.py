from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .currency import Currency
from .company import Company
from .finance_book import FinanceBook
# from .journal_entry_template import JournalEntryTemplate
# from .mode_of_payment import ModeOfPayment
# from .payment_entry import ModeofPayment
# from .payment_order import PaymentOrder



class JournalEntry(models.Model):
    title = models.CharField(max_length=150, blank=True)
    posting_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    finance_book = models.ForeignKey(FinanceBook, on_delete=CASCADE, blank=True, null=True)
    cheque_no = models
    cheque_date = models.CharField(max_length=150, blank=True)
    user_remark = models.TextField()
    total_debit = models.DecimalField(max_digits=20, decimal_places=2)
    total_credit = models.DecimalField(max_digits=20, decimal_places=2)
    difference = models.DecimalField(max_digits=20, decimal_places=2)
    total_amount_currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    total_amount_in_words = models.CharField(max_length=150, blank=True)
    clearance_date = models.DateField(auto_now_add=True)
    remark = models.TextField()
    paid_loan = models.CharField(max_length=150, blank=True)
    bill_no = models.CharField(max_length=150, blank=True)
    bill_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    write_off_amount = models.DecimalField(max_digits=20, decimal_places=2)
    pay_to_recd_from = models.CharField(max_length=150, blank=True)
    # letter_head = models.ForeignKey(LetterHead, on_delete=CASCADE, blank=True, null=True)
    # mode_of_payment = models.ForeignKey(ModeofPayment, on_delete=CASCADE, blank=True, null=True)
    # payment_order = models.ForeignKey(PaymentOrder, on_delete=CASCADE, blank=True, null=True)
    # stock_entry = models.ForeignKey(StockEntry, on_delete=CASCADE, blank=True, null=True)
    # auto_repeat = models.ForeignKey(AutoRepeat, on_delete=CASCADE, blank=True, null=True)
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    # from_template = models.ForeignKey(JournalEntryTemplate, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='journal_entry_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='journal_entry_modified_by')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "journal_entry"

#letterhead-fk
#mode_of_payment-fk
#payment_order-fk
#from_template-fk
#journal_entry_template-fk
#journal_entry-fk
#auto_repeat-fk
#stock_entry-fk
