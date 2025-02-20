from django.shortcuts import render, get_object_or_404

from cafe.models import Order, Item

def orders(request):
    return render(request, 'cafe/orders.html', {"orders": Order.objects.all()})

def create(request):
    max_item = 10
    if request.method == 'POST':
        tn = request.POST['table_number']
        if tn.isdigit():
            order = Order(table_number=int(tn), total_price=0.0, status='В ожидании')
            order.save()
            total_price = 0.0
            for i in range(max_item):
                item_name = request.POST['item' + str(i)]
                if item_name != '':
                    price = request.POST['price' + str(i)]
                    if price.isdigit():
                        price = float(price)
                        total_price += price
                        item = Item(order_id=order, item_name=item_name[:50], price=price)
                        item.save()
            order.total_price = total_price
            order.save()
            return render(request, 'cafe/created.html', {"id": order.id})
    return render(request, 'cafe/create.html', {"range": range(max_item)})

def edit(request):
    if request.method == 'POST':
        id = request.POST['id']
        if id.isdigit():
            order = get_object_or_404(Order, id=int(id))
            order.status = request.POST['status']
            order.save()
            return render(request, 'cafe/edited.html', {"id": id})
    return render(request, 'cafe/edit.html')

def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        if id.isdigit():
            order = get_object_or_404(Order, id=int(id))
            order.delete()
            return render(request, 'cafe/deleted.html', {"id": id})
    return render(request, 'cafe/delete.html')

def report(request):
    s = sum([x.total_price for x in Order.objects.filter(status="Оплачено")])
    return render(request, 'cafe/report.html', {"sum": s})

def search(request):
    if request.method == 'POST':
        string = request.POST['string']
        if string.isdigit():
            message = f'Заказы с номером стола {string}:'
            return render(request, 'cafe/search.html', {"orders": Order.objects.filter(table_number=int(string)), "message": message})
        elif string in ['В ожидании', 'Готово', 'Оплачено']:
            message = f'Заказы со статусом {string}:'
            return render(request, 'cafe/search.html', {"orders": Order.objects.filter(status=string), "message": message})
        else:
            message = f'Некорректный запрос: {string}:'
            return render(request, 'cafe/search.html', {"message": message})
    return render(request, 'cafe/search.html')

def home(request):
    return render(request, 'cafe/base.html')