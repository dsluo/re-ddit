from django.shortcuts import render

from django.db.models.functions import Lower

from base.models import SubjectArea

# Create your views here.


# Displays the index of the bulletin view. Includes a list of subject areas.
def index(request):
    # Obtain a list of subject areas from the database.
    list_of_subjects = SubjectArea.objects.order_by('long')

    # Create a dictionary containing the list.
    context = {
        'list_of_subjects': list_of_subjects,
    }

    # Pass the dictionary into the template for the index page.
    return render(request, 'bulletin/index.html', context)


# Displays the details page for a subject.
# This view includes a description of the subject and list of classes belonging
# to the subject.
def subject(request, subject_short):

    # Attempt to retrieve the subject object corresponding to the value passed
    # into the function by the URL.
    subject_object_list = SubjectArea.objects.filter(short__iexact=subject_short)

    if subject_object_list.count() == 0:  # then the subject doesn't exist.

        # Renders the template without a subject object. Template will display
        # an error message to the user.
        return render(request, 'bulletin/subject.html')

    else:  # the subject does exist.

        # Create a dictionary containing the subject object.
        context = {
            'subject': subject_object_list[0]
        }

        # Pass the object into the template for the subject view page.
        return render(request, 'bulletin/subject.html', context)


# Displays the details page for a single subject.
def course(request, subject_short, course_number):

    # Attempt to retrieve the subject object corresponding to the value passed
    # into the function by the URL.

    # If the subject doesn't exist...

        # Create a dictionary with an error string.

        # Render the template with the dictionary. Error string will be displayed.

    # Else...

        # Retrieve all Courses categorized under that Subject Area.

        # If the course doesn't exist...

            # Create a dictionary with an error string.

            # Render the template with the dictionary. Error string will be
            # displayed.

        # Else...

            # Create a dictionary containing the course object.

            # Pass the object into the template for the course view page.

    return render(request, 'bulletin/course.html')

