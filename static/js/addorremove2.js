function addorremove(id) {
    if (id){
    $.ajax({

        success:function() {
            $('#jobwl'+id).removeClass('btn-primary').addClass('btn-danger')
            const Toast = Swal.mixin({
              toast: true,
              position: 'top-end',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
              }
            })

            Toast.fire({
              icon: 'warning',
              title: 'you are not authorized!!'
    }
    });
    }

    }