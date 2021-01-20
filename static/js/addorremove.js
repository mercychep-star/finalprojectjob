  function addtomywishlist(id) {
    if (id){
    $.ajax({
        url:"/users/add-wishlist/" +id,
        method:"GET",
        success:function() {
            $('#jobwl'+id).removeClass('btn-primary').addClass('btn-danger')
            alert("success")
    }
    });
    }

    }
     function removefrommywishlist(id) {

    if (id){
    $.ajax({
        url:"/users/remove-from-wishlist/" +id,
        method:"GET",
        success:function() {
        $('#jobwl'+id).removeClass('btn-danger').addClass('btn-primary')
            alert("success")
    }
    });
    }

    }