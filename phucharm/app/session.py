from django.shortcuts import render

# Create and Manage your JWT Session here.
class Session:
    def _loader(self, request, context):
        return render(request, 'index.html', context)
