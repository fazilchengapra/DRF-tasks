from rest_framework.pagination import CursorPagination
class PaginationTest(CursorPagination):
    page_size=1
    ordering = '-id'
    