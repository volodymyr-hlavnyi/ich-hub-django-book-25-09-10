from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from first_app.models import Book

paginator = Paginator(Book.objects.all(), 5)
print(paginator.num_pages)
page_obj = paginator.page(2)

for book in page_obj:
    print(book)

print(paginator.count)
print(paginator.num_pages)
print(paginator.page_range)

# ----------------------

try:
    page_obj = paginator.page('utu')
except PageNotAnInteger:
    page_obj = paginator.page(1)
except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)

# -----------------
try:
    page_obj = paginator.page(100)
except PageNotAnInteger:
    page_obj = paginator.page(1)
except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)

# -----------------
from django.db.models import Avg, Max, Min, Sum
average_price = Book.objects.aggregate(avg_price=Avg('price'))
average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']
average_price

books_above_average = Book.objects.filter(price__gt=average_price)
books_above_average
for number, book in enumerate(books_above_average):
    print(number, book)

books2 = Book.objects.filter(price__gt=Book.objects.aggregate(avg_price=Avg('price'))['avg_price'])
for number, book in enumerate(books2):
    print(number, book)

# -------------------
from django.db.models import OuterRef, Subquery
subquery_min = Book.objects.filter(author = OuterRef('author')).value('author').annotate(min_price = Min('price')).values('min_price')
books3 = Book.objects.annotate(min_author_price = Subquery(subquery_min))
for num, book in enumerate(books3):
    print(num, book, book.price, book.min_author_price)

# ---------------------
