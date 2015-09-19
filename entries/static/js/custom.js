$( document ).ready(function() {


  // Object contains all votes taken in 2015 election 
  var votes_object = {
    "adana":["14", {"akp":"368.227"}, {"chp":"354.356"},{"mhp":"287.729"},{"hdp":"177.359"}],
    "adiyaman":["5", {"akp":"178.282"}, {"chp":"34.812"},{"mhp":"12.945"},{"hdp":"69.513"}],
    "afyonkarahisar":["5", {"akp":"222.467"}, {"chp":"71.131"},{"mhp":"108.115"},{"hdp":"4.446"}],
    "agri":["4", {"akp":"37.545"}, {"chp":"2.417"},{"mhp":"6.086"},{"hdp":"185.506"}],
    "aksaray":["3", {"akp":"119.659"}, {"chp":"13.669"},{"mhp":"62.110"},{"hdp":"3.540"}],
    "amasya":["3", {"akp":"95.876"}, {"chp":"54.928"},{"mhp":"48.017"},{"hdp":"2.465"}],
    "ankara_1_bolge":["18", {"akp":"653.136"}, {"chp":"603.076"},{"mhp":"328.252"},{"hdp":"111.603"}],
    "ankara_2_bolge":["14", {"akp":"667.389"}, {"chp":"340.472"},{"mhp":"249.165"},{"hdp":"56.031"}],
    "antalya":["14", {"akp":"456.645"}, {"chp":"429.075"},{"mhp":"287.161"},{"hdp":"90.644"}],
    "ardahan":["2", {"akp":"14.759"}, {"chp":"12.494"},{"mhp":"4.393"},{"hdp":"17.096"}], 
    "artvin":["2", {"akp":"41.982"}, {"chp":"33.528"},{"mhp":"24.820"},{"hdp":"2.943"}],
    "aydin":["7", {"akp":"192.688"}, {"chp":"267.395"},{"mhp":"119.539"},{"hdp":"58.254"}],
    "balikesir":["8", {"akp":"305.581"}, {"chp":"267.673"},{"mhp":"159.267"},{"hdp":"24.121"}],
    "bartin":["2", {"akp":"49.600"}, {"chp":"36.526"},{"mhp":"21.782"},{"hdp":"1.484"}],
    "batman":["4", {"akp":"47.921"}, {"chp":"2.083"},{"mhp":"2.748"},{"hdp":"191.309"}],
    "bayburt":["2", {"akp":"27.219"}, {"chp":"1.110"},{"mhp":"14.461"},{"hdp":"490"}],
    "bilecik":["2", {"akp":"49.172"}, {"chp":"38.833"},{"mhp":"34.006"},{"hdp":"4.349"}],
    "bingol":["3", {"akp":"61.294"}, {"chp":"1.622"},{"mhp":"3.652"},{"hdp":"53.519"}],
    "bitlis":["3", {"akp":"47.788"}, {"chp":"2.071"},{"mhp":"6.035"},{"hdp":"93.263"}],
    "bolu":["3", {"akp":"95.752"}, {"chp":"45.313"},{"mhp":"29.635"},{"hdp":"3.069"}],
    "burdur":["3", {"akp":"71.464"}, {"chp":"45.467"},{"mhp":"38.655"},{"hdp":"2.457"}],
    "bursa":["18", {"akp":"767.542"}, {"chp":"489.254"},{"mhp":"309.376"},{"hdp":"96.513"}],  
    "canakkale":["4", {"akp":"116.366"}, {"chp":"134.508"},{"mhp":"68.089"},{"hdp":"9.106"}],
    "cankiri":["2", {"akp":"64.316"}, {"chp":"7.213"},{"mhp":"30.962"},{"hdp":"914"}], 
    "corum":["4", {"akp":"180.281"}, {"chp":"74.268"},{"mhp":"59.108"},{"hdp":"6.134"}],
    "denizli":["7", {"akp":"247.998"}, {"chp":"220.526"},{"mhp":"115.016"},{"hdp":"23.849"}],
    "diyarbakir":["1", {"akp":"112.752"}, {"chp":"7.626"},{"mhp":"8.491"},{"hdp":"636.915"}],
    "duzce":["3", {"akp":"130.782"}, {"chp":"35.373"},{"mhp":"34.729"},{"hdp":"4.463"}],
    "edirne":["3", {"akp":"63.381"}, {"chp":"140.848"},{"mhp":"41.316"},{"hdp":"6.955"}],
    "elazig":["4", {"akp":"169.043"}, {"chp":"21.259"},{"mhp":"66.600"},{"hdp":"48.704"}],
    "erzincan":["4", {"akp":"63.916"}, {"chp":"33.153"},{"mhp":"21.687"},{"hdp":"7.161"}],
    "erzurum":["6", {"akp":"209.875"}, {"chp":"11.078"},{"mhp":"94.691"},{"hdp":"71.740"}],
    "eskisehir":["6", {"akp":"190.335"}, {"chp":"208.226"},{"mhp":"89.226"},{"hdp":"18.957"}],
    "gaziantep":["12", {"akp":"428.451"}, {"chp":"149.170"},{"mhp":"163.967"},{"hdp":"138.678"}],  
    "giresun":["4", {"akp":"139.740"}, {"chp":"57.454"},{"mhp":"48.374"},{"hdp":"2.599"}],
    "gumushane":["2", {"akp":"41.682"}, {"chp":"3.727"},{"mhp":"23.025"},{"hdp":"1.109"}],               
    "hakkari":["3", {"akp":"12.478"}, {"chp":"1.443"},{"mhp":"3.544"},{"hdp":"122.807"}],
    "hatay":["10", {"akp":"312.887"}, {"chp":"300.769"},{"mhp":"116.062"},{"hdp":"54.456"}],
    "igdir":["2", {"akp":"10.293"}, {"chp":"3.409"},{"mhp":"25.700"},{"hdp":"53.844"}],
    "isparta":["4", {"akp":"114.348"}, {"chp":"57.712"},{"mhp":"70.152"},{"hdp":"4.680"}],
    "istanbul_1_bolge":["31", {"akp":"1.231.914"}, {"chp":"972.323"},{"mhp":"320.010"},{"hdp":"320.834"}],
    "istanbul_2_bolge":["26", {"akp":"1.044.086"}, {"chp":"675.677"},{"mhp":"274.888"},{"hdp":"301.182"}],
    "istanbul_3_bolge":["31", {"akp":"1.117.251"}, {"chp":"791.904"},{"mhp":"323.458"},{"hdp":"408.745"}],
    "izmir_1_bolge":["13", {"akp":"335.032"}, {"chp":"572.433"},{"mhp":"165.043"},{"hdp":"147.636"}],
    "izmir_2_bolge":["13", {"akp":"358.953"}, {"chp":"629.712"},{"mhp":"198.021"},{"hdp":"125.453"}],
    "kahramanmaras":["8", {"akp":"352.949"}, {"chp":"49.112"},{"mhp":"115.291"},{"hdp":"29.749"}], 
    "karabuk":["2", {"akp":"67.540"}, {"chp":"24.292"},{"mhp":"38.902"},{"hdp":"1.578"}],
    "karaman":["2", {"akp":"80.042"}, {"chp":"22.366"},{"mhp":"32.876"},{"hdp":"1.724"}],
    "kars":["3", {"akp":"38.950"}, {"chp":"17.485"},{"mhp":"20.507"},{"hdp":"64.315"}],
    "kastamonu":["3", {"akp":"111.835"}, {"chp":"42.791"},{"mhp":"62.563"},{"hdp":"1.528"}],
    "kayseri":["9", {"akp":"409.658"}, {"chp":"97.165"},{"mhp":"217.384"},{"hdp":"18.070"}],
    "kirikkale":["3", {"akp":"81.710"}, {"chp":"24.733"},{"mhp":"46.610"},{"hdp":"2.037"}],
    "kirklareli":["3", {"akp":"53.399"}, {"chp":"115.951"},{"mhp":"49.487"},{"hdp":"5.342"}],
    "kirsehir":["2", {"akp":"52.732"}, {"chp":"25.762"},{"mhp":"42.801"},{"hdp":"8.121"}],
    "kilis":["2", {"akp":"32.279"}, {"chp":"5.042"},{"mhp":"23.375"},{"hdp":"2.428"}],
    "kocaeli":["11", {"akp":"487.537"}, {"chp":"256.787"},{"mhp":"161.459"},{"hdp":"77.540"}],
    "konya":["14", {"akp":"798.526"}, {"chp":"118.822"},{"mhp":"200.395"},{"hdp":"50.773"}],  
    "kutahya":["4", {"akp":"200.101"}, {"chp":"43.586"},{"mhp":"98.882"},{"hdp":"3.216"}],
    "malatya":["6", {"akp":"257.413"}, {"chp":"72.881"},{"mhp":"50.084"},{"hdp":"34.758"}], 
    "manisa":["9", {"akp":"327.012"}, {"chp":"259.396"},{"mhp":"210.986"},{"hdp":"59.717"}],
    "mardin":["6", {"akp":"72.645"}, {"chp":"3.736"},{"mhp":"4.187"},{"hdp":"276.920"}],
    "mersin":["11", {"akp":"266.717"}, {"chp":"298.362"},{"mhp":"255.740"},{"hdp":"183.934"}],
    "mugla":["6", {"akp":"148.527"}, {"chp":"257.460"},{"mhp":"106.248"},{"hdp":"28.747"}],
    "mus":["3", {"akp":"46.940"}, {"chp":"2.110"},{"mhp":"3.606"},{"hdp":"137.878"}],
    "nevsehir":["3", {"akp":"90.819"}, {"chp":"25.851"},{"mhp":"47.983"},{"hdp":"2.414"}],
    "nigde":["3", {"akp":"91.065"}, {"chp":"40.701"},{"mhp":"48.686"},{"hdp":"2.274"}],
    "ordu":["5", {"akp":"221.204"}, {"chp":"118.932"},{"mhp":"53.927"},{"hdp":"3.422"}],
    "osmaniye":["4", {"akp":"108.756"}, {"chp":"37.330"},{"mhp":"114.990"},{"hdp":"10.735"}],
    "rize":["3", {"akp":"131.168"}, {"chp":"37.110"},{"mhp":"15.870"},{"hdp":"2.232"}],
    "sakarya":["7", {"akp":"324.001"}, {"chp":"90.733"},{"mhp":"111.127"},{"hdp":"14.772"}],
    "samsun":["9", {"akp":"399.504"}, {"chp":"174.557"},{"mhp":"134.797"},{"hdp":"8.878"}],
    "siirt":["3", {"akp":"40.030"}, {"chp":"1.722"},{"mhp":"3.349"},{"hdp":"93.513"}],
    "sinop":["2", {"akp":"60.087"}, {"chp":"36.271"},{"mhp":"21.453"},{"hdp":"1.563"}],
    "sivas":["5", {"akp":"212.734"}, {"chp":"55.257"},{"mhp":"67.145"},{"hdp":"5.036"}],
    "sanliurfa":["12", {"akp":"356.537"}, {"chp":"31.273"},{"mhp":"42.479"},{"hdp":"293.841"}],
    "sirnak":["4", {"akp":"19.366"}, {"chp":"2.101"},{"mhp":"5.248"},{"hdp":"188.002"}],
    "tekirdag":["6", {"akp":"177.458"}, {"chp":"253.295"},{"mhp":"86.333"},{"hdp":"31.543"}],
    "tokat":["5", {"akp":"180.489"}, {"chp":"72.916"},{"mhp":"76.872"},{"hdp":"4.430"}],
    "trabzon":["6", {"akp":"253.418"}, {"chp":"77.784"},{"mhp":"96.086"},{"hdp":"4.033"}],
    "tunceli":["2", {"akp":"5.631"}, {"chp":"10.906"},{"mhp":"3.131"},{"hdp":"32.241"}],
    "usak":["3", {"akp":"86.399"}, {"chp":"64.442"},{"mhp":"63.310"},{"hdp":"5.422"}],
    "van":["8", {"akp":"95.477"}, {"chp":"13.318"},{"mhp":"4.841"},{"hdp":"368.516"}],
    "yalova":["2", {"akp":"54.366"}, {"chp":"40.065"},{"mhp":"26.778"},{"hdp":"11.422"}],
    "yozgat":["4", {"akp":"139.934"}, {"chp":"21.626"},{"mhp":"66.958"},{"hdp":"2.297"}],
    "zonguldak":["5", {"akp":"142.329"}, {"chp":"146.162"},{"mhp":"61.500"},{"hdp":"4.399"}],
  }

  // Text cleaner
  function clean_text(text_input){

    var text_output = text_input.toUpperCase();

    text_output = text_output.replace('.', '');
    text_output = text_output.replace(/ /g, '_');
    text_output = text_output.replace(/Ö/g, 'O');
    text_output = text_output.replace(/Ş/g, 'S');
    text_output = text_output.replace(/İ/g, 'I');
    text_output = text_output.replace(/Ğ/g, 'G');
    text_output = text_output.replace(/Ç/g, 'C');
    text_output = text_output.replace(/Ü/g, 'U');

    var text_output = text_output.toLowerCase();

    return text_output;
  }

  function sortNumber(a,b) { 
    return a - b; 
  }

  function calculate_deputy() {

    // $('#results').on('click', function() {

    // Votes
    var akp_vote = $('#akp').val();
    akp_vote = akp_vote.replace('.', ''); akp_vote = akp_vote.replace('.', '');
    var chp_vote = $('#chp').val();
    chp_vote = chp_vote.replace('.', ''); chp_vote = chp_vote.replace('.', '');
    var mhp_vote = $('#mhp').val();
    mhp_vote = mhp_vote.replace('.', ''); mhp_vote = mhp_vote.replace('.', '');
    var hdp_vote = $('#hdp').val();
    hdp_vote = hdp_vote.replace('.', ''); hdp_vote = hdp_vote.replace('.', ''); 

    // Additional votes
    var akp_addition = $('#akp_addition').val();
    akp_addition = akp_addition.replace('.', ''); akp_addition = akp_addition.replace('.', '');
    var chp_addition = $('#chp_addition').val();
    chp_addition = chp_addition.replace('.', ''); chp_addition = chp_addition.replace('.', '');
    var mhp_addition = $('#mhp_addition').val();
    mhp_addition = mhp_addition.replace('.', ''); mhp_addition = mhp_addition.replace('.', '');
    var hdp_addition = $('#hdp_addition').val();
    hdp_addition = hdp_addition.replace('.', ''); hdp_addition = hdp_addition.replace('.', ''); 

    // Calculate total votes
    akp_vote = Number(akp_vote) + Number(akp_addition);
    mhp_vote = Number(mhp_vote) + Number(mhp_addition);
    chp_vote = Number(chp_vote) + Number(chp_addition);
    hdp_vote = Number(hdp_vote) + Number(hdp_addition);

    console.log(akp_vote);

    // All votes
    var all_votes = [];
    all_votes['akp'] = akp_vote;
    all_votes['chp'] = chp_vote;
    all_votes['mhp'] = mhp_vote;
    all_votes['hdp'] = hdp_vote;

    // Deputy numbers
    var total_deputy = Number($('#total_deputy').val());
    var current_deputy = 0;
    var akp_deputy = 0;
    var chp_deputy = 0;
    var mhp_deputy = 0;
    var hdp_deputy = 0;

    // Calculate deputies
    while (current_deputy < total_deputy) {

      var vote_list = [all_votes['akp'], all_votes['chp'], all_votes['mhp'], all_votes['hdp']];
      var vote_list_tmp = [all_votes['akp'], all_votes['chp'], all_votes['mhp'], all_votes['hdp']];
      var vote_list_sorted = vote_list_tmp.sort(sortNumber).reverse();
      var high_vote = vote_list_sorted[0];

      if (all_votes['akp'] == high_vote) {
        akp_deputy = akp_deputy + 1;
        all_votes['akp'] = akp_vote / (akp_deputy + 1);
      
      } else if (all_votes['chp'] == high_vote) {
        chp_deputy = chp_deputy + 1;
        all_votes['chp'] = chp_vote / (chp_deputy + 1);

      } else if (all_votes['mhp'] == high_vote) {
        mhp_deputy = mhp_deputy + 1;
        all_votes['mhp'] = mhp_vote / (mhp_deputy + 1);

      } else if (all_votes['hdp'] == high_vote) {
        hdp_deputy = hdp_deputy + 1;
        all_votes['hdp'] = hdp_vote / (hdp_deputy + 1);

      }

      current_deputy = current_deputy + 1
      vote_list_tmp = vote_list;

      // if (akp_situation) {
      //   vote_list_tmp[0] = vote_list_tmp[0] + '*'
      // } else if (chp_situation) {
      //   vote_list_tmp[1] = vote_list_tmp[1] + '*'
      // } else if (mhp_situation) {
      //   vote_list_tmp[2] = vote_list_tmp[2] + '*'
      // } else if (dhp_situation) {
      //   vote_list_tmp[3] = vote_list_tmp[3] + '*'
      // }

      // $('#votes'+current_deputy).text(vote_list_tmp);
    }

    $('#akp_deputy_result').val(akp_deputy);
    $('#chp_deputy_result').val(chp_deputy);
    $('#mhp_deputy_result').val(mhp_deputy);
    $('#hdp_deputy_result').val(hdp_deputy);
  }

  // var e = document.getElementById("ddlViewBy");
  // var strUser = e.options[e.selectedIndex].value;
  // $('.input_field_id').on('input', dropdown_function);

  $("#locations").change(function () {

    var choice = $('#locations').val();
    var cleaned_choice = clean_text(choice);

    $('#akp').val(votes_object[cleaned_choice][1]['akp']);
    $('#chp').val(votes_object[cleaned_choice][2]['chp']);
    $('#mhp').val(votes_object[cleaned_choice][3]['mhp']);
    $('#hdp').val(votes_object[cleaned_choice][4]['hdp']);

    $('#akp_addition').val('0');
    $('#chp_addition').val('0');
    $('#mhp_addition').val('0');
    $('#hdp_addition').val('0');

    $('#total_deputy').val(votes_object[cleaned_choice][0]);

    calculate_deputy();
  });

  $(".input_fields").on('input', function () {

    calculate_deputy(); 
  });
});








