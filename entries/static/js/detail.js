$(document).ready(function() {

    $('#show-comment').on('click', function() {
        $(this).hide();
        $('#comment').show();
    })

    $('#hide-comment').on('click', function() {
        $('#comment').hide();
        $('#show-comment').show();
    })

    //

    $('.show_subcomment').on('click', function() {

        $('.twosubcomments').hide()
        $('.show_twosubcomment').show()
        $('.subcomments').hide()
        $('.show_subcomment').show()
        var commentID = this.id.split("-")[2];
        $('#subcomment-' + commentID).show();
        $(this).hide();
    })

    $('.hide-subcomment').on('click', function() {

        var commentID = this.id.split("-")[2];
        $('#subcomment-' + commentID).hide();
        $('#show-subcomment-' + commentID).show();

    })

    //

    $('.show_twosubcomment').on('click', function() {

        $('.twosubcomments').hide()
        $('.show_twosubcomment').show()
        $('.subcomments').hide()
        $('.show_subcomment').show()
        var subcommentID = this.id.split("-")[2];
        $('#twosubcomment-' + subcommentID).show();
        $(this).hide();
    })

    $('.hide-twosubcomment').on('click', function() {

        var subcommentID = this.id.split("-")[2];
        $('#twosubcomment-' + subcommentID).hide();
        $('#show-twosubcomment-' + subcommentID).show();

    })

// FOR COMMNETS

$('.button_up').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).hide();
    $('#arrow-up2-' + commentID).show();
    $('#arrow-up3-' + commentID).hide();
    $('#arrow-down-' + commentID).hide();
    $('#arrow-down2-' + commentID).hide();
    $('#arrow-down3-' + commentID).show();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-" + commentID).textContent = vote })


$('.button_up2').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).show();
    $('#arrow-up2-' + commentID).hide();
    $('#arrow-up3-' + commentID).hide();
    $('#arrow-down-' + commentID).show();
    $('#arrow-down2-' + commentID).hide();
    $('#arrow-down3-' + commentID).hide();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-" + commentID).textContent = vote })

$('.button_up3').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).hide();
    $('#arrow-up2-' + commentID).show();
    $('#arrow-up3-' + commentID).hide();
    $('#arrow-down-' + commentID).hide();
    $('#arrow-down2-' + commentID).hide();
    $('#arrow-down3-' + commentID).show();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) + 2;
    document.getElementById("rate-" + commentID).textContent = vote })

$('.button_down').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).hide();
    $('#arrow-up2-' + commentID).hide();
    $('#arrow-up3-' + commentID).show();
    $('#arrow-down-' + commentID).hide();
    $('#arrow-down2-' + commentID).show();
    $('#arrow-down3-' + commentID).hide();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-" + commentID).textContent = vote })

$('.button_down2').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).show();
    $('#arrow-up2-' + commentID).hide();
    $('#arrow-up3-' + commentID).hide();
    $('#arrow-down-' + commentID).show();
    $('#arrow-down2-' + commentID).hide();
    $('#arrow-down3-' + commentID).hide();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-" + commentID).textContent = vote })

$('.button_down3').on('click', function() {

    var commentID = this.id.split("-")[2];
    $('#arrow-up-' + commentID).hide();
    $('#arrow-up2-' + commentID).hide();
    $('#arrow-up3-' + commentID).show();
    $('#arrow-down-' + commentID).hide();
    $('#arrow-down2-' + commentID).show();
    $('#arrow-down3-' + commentID).hide();
    var content = document.getElementById("rate-" + commentID).textContent;
    var vote = parseInt(content) - 2;
    document.getElementById("rate-" + commentID).textContent = vote })

// FOR SUBCOMMNETS

$('.subutton_up').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).hide();
    $('#subarrow-up2-' + subcommentID).show();
    $('#subarrow-up3-' + subcommentID).hide();
    $('#subarrow-down-' + subcommentID).hide();
    $('#subarrow-down2-' + subcommentID).hide();
    $('#subarrow-down3-' + subcommentID).show();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })


$('.subutton_up2').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).show();
    $('#subarrow-up2-' + subcommentID).hide();
    $('#subarrow-up3-' + subcommentID).hide();
    $('#subarrow-down-' + subcommentID).show();
    $('#subarrow-down2-' + subcommentID).hide();
    $('#subarrow-down3-' + subcommentID).hide();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })

$('.subutton_up3').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).hide();
    $('#subarrow-up2-' + subcommentID).show();
    $('#subarrow-up3-' + subcommentID).hide();
    $('#subarrow-down-' + subcommentID).hide();
    $('#subarrow-down2-' + subcommentID).hide();
    $('#subarrow-down3-' + subcommentID).show();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) + 2;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })

$('.subutton_down').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).hide();
    $('#subarrow-up2-' + subcommentID).hide();
    $('#subarrow-up3-' + subcommentID).show();
    $('#subarrow-down-' + subcommentID).hide();
    $('#subarrow-down2-' + subcommentID).show();
    $('#subarrow-down3-' + subcommentID).hide();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })

$('.subutton_down2').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).show();
    $('#subarrow-up2-' + subcommentID).hide();
    $('#subarrow-up3-' + subcommentID).hide();
    $('#subarrow-down-' + subcommentID).show();
    $('#subarrow-down2-' + subcommentID).hide();
    $('#subarrow-down3-' + subcommentID).hide();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })

$('.subutton_down3').on('click', function() {

    var subcommentID = this.id.split("-")[2];
    $('#subarrow-up-' + subcommentID).hide();
    $('#subarrow-up2-' + subcommentID).hide();
    $('#subarrow-up3-' + subcommentID).show();
    $('#subarrow-down-' + subcommentID).hide();
    $('#subarrow-down2-' + subcommentID).show();
    $('#subarrow-down3-' + subcommentID).hide();
    var content = document.getElementById("rate-subcomment-" + subcommentID).textContent;
    var vote = parseInt(content) - 2;
    document.getElementById("rate-subcomment-" + subcommentID).textContent = vote })

// FOR TWOSUBCOMMNETS

$('.twosubutton_up').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).hide();
    $('#twosubarrow-up2-' + twosubcommentID).show();
    $('#twosubarrow-up3-' + twosubcommentID).hide();
    $('#twosubarrow-down-' + twosubcommentID).hide();
    $('#twosubarrow-down2-' + twosubcommentID).hide();
    $('#twosubarrow-down3-' + twosubcommentID).show();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })


$('.twosubutton_up2').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).show();
    $('#twosubarrow-up2-' + twosubcommentID).hide();
    $('#twosubarrow-up3-' + twosubcommentID).hide();
    $('#twosubarrow-down-' + twosubcommentID).show();
    $('#twosubarrow-down2-' + twosubcommentID).hide();
    $('#twosubarrow-down3-' + twosubcommentID).hide();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })

$('.twosubutton_up3').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).hide();
    $('#twosubarrow-up2-' + twosubcommentID).show();
    $('#twosubarrow-up3-' + twosubcommentID).hide();
    $('#twosubarrow-down-' + twosubcommentID).hide();
    $('#twosubarrow-down2-' + twosubcommentID).hide();
    $('#twosubarrow-down3-' + twosubcommentID).show();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) + 2;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })

$('.twosubutton_down').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).hide();
    $('#twosubarrow-up2-' + twosubcommentID).hide();
    $('#twosubarrow-up3-' + twosubcommentID).show();
    $('#twosubarrow-down-' + twosubcommentID).hide();
    $('#twosubarrow-down2-' + twosubcommentID).show();
    $('#twosubarrow-down3-' + twosubcommentID).hide();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })

$('.twosubutton_down2').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).show();
    $('#twosubarrow-up2-' + twosubcommentID).hide();
    $('#twosubarrow-up3-' + twosubcommentID).hide();
    $('#twosubarrow-down-' + twosubcommentID).show();
    $('#twosubarrow-down2-' + twosubcommentID).hide();
    $('#twosubarrow-down3-' + twosubcommentID).hide();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })

$('.twosubutton_down3').on('click', function() {

    var twosubcommentID = this.id.split("-")[2];
    $('#twosubarrow-up-' + twosubcommentID).hide();
    $('#twosubarrow-up2-' + twosubcommentID).hide();
    $('#twosubarrow-up3-' + twosubcommentID).show();
    $('#twosubarrow-down-' + twosubcommentID).hide();
    $('#twosubarrow-down2-' + twosubcommentID).show();
    $('#twosubarrow-down3-' + twosubcommentID).hide();
    var content = document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent;
    var vote = parseInt(content) - 2;
    document.getElementById("rate-twosubcomment-" + twosubcommentID).textContent = vote })

// FOR TITLE THUMBS UP AND DOWN

$('.thumbs_up').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).hide();
    $('#thumbs-up2-' + entryID).show();
    $('#thumbs-up3-' + entryID).hide();
    $('#thumbs-down-' + entryID).hide();
    $('#thumbs-down2-' + entryID).hide();
    $('#thumbs-down3-' + entryID).show();
    $('#up_title').show();
    $('#down_title').hide();
    $('#none_title').hide();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("title-rate-" + entryID).textContent = vote })

$('.thumbs_up2').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).show();
    $('#thumbs-up2-' + entryID).hide();
    $('#thumbs-up3-' + entryID).hide();
    $('#thumbs-down-' + entryID).show();
    $('#thumbs-down2-' + entryID).hide();
    $('#thumbs-down3-' + entryID).hide();
    $('#up_title').hide();
    $('#down_title').hide();
    $('#none_title').show();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("title-rate-" + entryID).textContent = vote })

$('.thumbs_up3').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).hide();
    $('#thumbs-up2-' + entryID).show();
    $('#thumbs-up3-' + entryID).hide();
    $('#thumbs-down-' + entryID).hide();
    $('#thumbs-down2-' + entryID).hide();
    $('#thumbs-down3-' + entryID).show();
    $('#up_title').show();
    $('#down_title').hide();
    $('#none_title').hide();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) + 2;
    document.getElementById("title-rate-" + entryID).textContent = vote })

$('.thumbs_down').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).hide();
    $('#thumbs-up2-' + entryID).hide();
    $('#thumbs-up3-' + entryID).show();
    $('#thumbs-down-' + entryID).hide();
    $('#thumbs-down2-' + entryID).show();
    $('#thumbs-down3-' + entryID).hide();
    $('#up_title').hide();
    $('#down_title').show();
    $('#none_title').hide();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) - 1;
    document.getElementById("title-rate-" + entryID).textContent = vote })

$('.thumbs_down2').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).show();
    $('#thumbs-up2-' + entryID).hide();
    $('#thumbs-up3-' + entryID).hide();
    $('#thumbs-down-' + entryID).show();
    $('#thumbs-down2-' + entryID).hide();
    $('#thumbs-down3-' + entryID).hide();
    $('#up_title').hide();
    $('#down_title').hide();
    $('#none_title').show();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) + 1;
    document.getElementById("title-rate-" + entryID).textContent = vote })

$('.thumbs_down3').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#thumbs-up-' + entryID).hide();
    $('#thumbs-up2-' + entryID).hide();
    $('#thumbs-up3-' + entryID).show();
    $('#thumbs-down-' + entryID).hide();
    $('#thumbs-down2-' + entryID).show();
    $('#thumbs-down3-' + entryID).hide();
    $('#up_title').hide();
    $('#down_title').show();
    $('#none_title').hide();
    var content = document.getElementById("title-rate-" + entryID).textContent;
    var vote = parseInt(content) - 2;
    document.getElementById("title-rate-" + entryID).textContent = vote })

})