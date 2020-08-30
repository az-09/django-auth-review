### Part 2
    django-guardian: permission for object instance level
    
    assign a permission to user: 
    
        perm = Permission.objects.get(codename='view_surveyassignment')

        assign_perm(perm, assigned_to, assigned_survey)

    assign a permission to group:

        group = Group.objects.create(name=f"survey_{survey.id}_result_viewers")
        
        assign_perm('can_view_results', group, survey)



Reference
https://thecodinginterface.com/blog/django-auth-part1/

https://thecodinginterface.com/blog/django-auth-part2/


