$(document).ready(function() {

    $('#show-comment').on('click', function() {

        $(this).hide();
        $('#comment').show();

    })

    $('#hide-comment').on('click', function() {

        $('#comment').hide();
        $('#show-comment').show();

    })

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