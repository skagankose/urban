$(document).ready(function() {

$('.button_up').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).hide();
    $('#arrow-up2-' + entryID).show();
    $('#arrow-up3-' + entryID).hide();
    $('#arrow-down-' + entryID).hide();
    $('#arrow-down2-' + entryID).hide();
    $('#arrow-down3-' + entryID).show();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) + 1;
    document.getElementById("rate-" + entryID).textContent = vote })


$('.button_up2').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).show();
    $('#arrow-up2-' + entryID).hide();
    $('#arrow-up3-' + entryID).hide();
    $('#arrow-down-' + entryID).show();
    $('#arrow-down2-' + entryID).hide();
    $('#arrow-down3-' + entryID).hide();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) - 1;
    document.getElementById("rate-" + entryID).textContent = vote })

$('.button_up3').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).hide();
    $('#arrow-up2-' + entryID).show();
    $('#arrow-up3-' + entryID).hide();
    $('#arrow-down-' + entryID).hide();
    $('#arrow-down2-' + entryID).hide();
    $('#arrow-down3-' + entryID).show();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) + 2;
    document.getElementById("rate-" + entryID).textContent = vote })

$('.button_down').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).hide();
    $('#arrow-up2-' + entryID).hide();
    $('#arrow-up3-' + entryID).show();
    $('#arrow-down-' + entryID).hide();
    $('#arrow-down2-' + entryID).show();
    $('#arrow-down3-' + entryID).hide();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) - 1;
    document.getElementById("rate-" + entryID).textContent = vote })

$('.button_down2').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).show();
    $('#arrow-up2-' + entryID).hide();
    $('#arrow-up3-' + entryID).hide();
    $('#arrow-down-' + entryID).show();
    $('#arrow-down2-' + entryID).hide();
    $('#arrow-down3-' + entryID).hide();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) + 1;
    document.getElementById("rate-" + entryID).textContent = vote })

$('.button_down3').on('click', function() {

    var entryID = this.id.split("-")[2];
    $('#arrow-up-' + entryID).hide();
    $('#arrow-up2-' + entryID).hide();
    $('#arrow-up3-' + entryID).show();
    $('#arrow-down-' + entryID).hide();
    $('#arrow-down2-' + entryID).show();
    $('#arrow-down3-' + entryID).hide();
    var content = document.getElementById("rate-" + entryID).textContent;
    var vote = parseInt(content.split('/')[0]) - 2;
    document.getElementById("rate-" + entryID).textContent = vote })

})
