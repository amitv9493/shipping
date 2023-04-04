from django.shortcuts import render

# Create your views here.


# from blabel import LabelWriter

def label_gen(request):
    # label_writer = LabelWriter("item_template.html",
    #                         default_stylesheets=("css/style.css",))
    # records= [
    #     dict(sample_id="s01", sample_name="Sample 1"),
    #     dict(sample_id="s02", sample_name="Sample 2")
    # ]

    # label_writer.write_labels(records, target='qrcode_and_label.pdf')
    return render(request, "item_template.html", context={})
    