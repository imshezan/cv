
from django.http import HttpResponse


# Create your views here.
#function based view
def home(request):
    html_ = """
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    
        <title>Shezan Mahmd.</title>


                     <style>
    div {
        
        border: 1px solid black;
        margin-top: 100px;
        margin-bottom: 100px;
        margin-right: 300px;
        margin-left: 300px;
    
        background-color: 	#e6ffff;
    }
    </style>
 

    </head>
        <body>
      
          <div>
      
      
      
      
      
             <table style="width: 100.0%;" width="100%">
              <tbody>
                <tr>
                <td style="padding: .75pt .75pt .75pt .75pt;">&nbsp;</td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="padding: 0in 0in 0in 0in;">
                <table style="width: 100.0%;" width="100%">
                <tbody>
                <tr>
                <td style="width: 73%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 12pt 0in 2.65pt 5.25pt;" width="73%">
                <p><strong><span style="font-size: 13.5pt; font-family: 'Verdana','sans-serif'; color: #333399;">SHEZAN MAHMUD </span></strong></p>
                </td>
                <td style="width: 27.0%; padding: 0in 0in 0in 0in;" rowspan="2" width="27%">
                <table style="width: 105.0pt; background: #DADCE1;" width="140">
                <tbody>
                <tr style="height: 101.25pt;">
                <td style="width: 94.5pt; background: #E2E4E5; padding: 0in 0in 0in 0in; height: 101.25pt;" width="126">&nbsp;</td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Address: 1/A, Block - D, Road - 8, Arifabad Housing(Near Milk vita), Mirpur-7, Dhaka- 1216. <br />Mobile No 1: 01557711220 <br />e-mail : amishezanmahmud@gmail.com</span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="border: none; border-bottom: solid black 1.0pt; padding: 0in 0in 0in 0in;">
                <p>&nbsp;</p>
                </td>
                </tr>
                <tr>
                <td style="padding: 0in 0in 0in 0in;">
                <p>&nbsp;</p>
                </td>
                </tr>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Career Objective:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">To take a challenging and managerial role in the field of Computer programming and implement the expertise and experience gained in this field to develop complex project with efficiency and quality. </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Special Qualification:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">python3, Django, Javascript, Bootstrap, C#(Asp.net), UI/UX design, SQLite, My SQL, Data Analysis, HTML, CSS, CMS, Troubleshooting hardware and network(Cisco &amp; MAN), MS Word+Powerpoint, Adobe(Ps, Ai), Gif Making. </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Academic Qualification:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <table style="width: 100.0%; border: solid #666666 1.0pt;" width="100%">
                <tbody>
                <tr>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Exam Title</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Concentration/Major</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Institute</span></strong></p>
                </td>
                <td style="width: 12%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Result</span></strong></p>
                </td>
                <td style="width: 12%; border: none; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Pas.Year</span></strong></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Diploma in Engineering &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Computer Technology &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bhola Polytechnic Institute. &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">pass &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">2017 &nbsp; </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Secondary School Certificate &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Science &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Daulatkhan Govt. High School &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">CGPA:4.44<br />out of 5 &nbsp;</span></p>
                </td>
                <td style="width: 12%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">2010 &nbsp; </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Training Summary:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <table style="width: 100.0%; border: solid #666666 1.0pt;" width="100%">
                <tbody>
                <tr>
                <td style="width: 19%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="19%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Training Title</span></strong></p>
                </td>
                <td style="width: 19%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="19%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Topic</span></strong></p>
                </td>
                <td style="width: 15%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Institute</span></strong></p>
                </td>
                <td style="width: 15%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Country</span></strong></p>
                </td>
                <td style="width: 15%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Location</span></strong></p>
                </td>
                <td style="width: 2%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="2%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Year</span></strong></p>
                </td>
                <td style="width: 15%; border: none; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Duration</span></strong></p>
                </td>
                </tr>
                <tr>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Advanced Python 3 Programming &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 0.75pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">python 3 and Django &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">BITM (Basis) and LEADS training joint venture &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bangladesh &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Rupayan T-Center. 16th Floor, Bangla Motor, Dhaka &nbsp; </span></p>
                </td>
                <td style="width: 10%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="10%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">2017 &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">3 Month &nbsp; </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Web Design and Development &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 0.75pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">HTML, CSS, MySql, php(Introduction), &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Open It Ltd. &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bangladesh &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">1283, Begum Rokeya Sarani, Mirpur-10, Dhaka-1216. &nbsp; </span></p>
                </td>
                <td style="width: 10%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="10%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">2016 &nbsp; </span></p>
                </td>
                <td style="width: 15%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="15%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">3 month &nbsp; </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Professional Qualification:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <table style="width: 100.0%; border: solid #666666 1.0pt;" width="100%">
                <tbody>
                <tr>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Certification</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Institute</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Location</span></strong></p>
                </td>
                <td style="width: 12%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">From</span></strong></p>
                </td>
                <td style="width: 12%; border: none; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">To</span></strong></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Advanced Python 3 Programming &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">jointly organized by BITM &amp; Leads Training &amp; Consulting Ltd &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Kazi Nazrul Islam Avenue Dhaka, Bangladesh. &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">July 24, 2017 &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">October 23, 2017 &nbsp; </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Web Designer &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Open IT(BD) LTD. &nbsp; </span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Begum Rokeya Saroni, Dhaka, Bangladesh. &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">September 16, 2016 &nbsp; </span></p>
                </td>
                <td style="width: 12%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="12%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">December 16, 2016 &nbsp; </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Career and Application Information:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 1.5pt;">
                <table style="width: 100.0%;" width="100%">
                <tbody>
                <tr>
                <td style="width: 32%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="32%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Looking For</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 66%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="66%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Entry Level Job </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 32%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="32%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Available For</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 66%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="66%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Full Time </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 32%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="32%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Preferred Job Category</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 66%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="66%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Engineer/Architect, IT/Telecommunication </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 32%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="32%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Preferred District </span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 66%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="66%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Dhaka </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 32%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="32%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Preferred Organization Types</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 66%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="66%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Software Company </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Specialization:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <table style="width: 562.5pt; border: solid #666666 1.0pt;" width="750">
                <tbody>
                <tr>
                <td style="width: 40%; border-top: none; border-right: none; border-left: none; border-image: initial; border-bottom: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="40%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Fields of Specialization</span></strong></p>
                </td>
                </tr>
                <tr>
                <td style="width: 40%; border: none; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="40%">
                <ul>
                <li><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Python</span></li>
                <li><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bootstrap</span></li>
                <li><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">django</span></li>
                <li><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">SQLite</span></li>
                <li><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">UI/UX Design</span></li>
                </ul>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';"><br />&nbsp;</span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Extra Curricular Activities:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Links:: https://amishezan.blogspot.com/ https://github.com/imshezan https://fb.com/amishezan https://linkedin.com/in/shezanmahmud/ </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Language Proficiency:</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 3.75pt;">
                <table style="width: 562.5pt; border: solid #666666 1.0pt;" width="750">
                <tbody>
                <tr>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Language</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Reading</span></strong></p>
                </td>
                <td style="width: 25%; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Writing</span></strong></p>
                </td>
                <td style="width: 25%; border: none; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><strong><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Speaking</span></strong></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bengali&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">High&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">High&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">High&nbsp;</span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">English&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Medium&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-top: 1pt solid #666666; border-left: none; border-bottom: none; border-right: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Medium&nbsp;</span></p>
                </td>
                <td style="width: 25%; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1pt solid #666666; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 1.5pt;" width="25%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Medium&nbsp;</span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif'; display: none;">&nbsp;</span></p>
                <table style="width: 562.5pt;" width="750">
                <tbody>
                <tr>
                <td style="background: #E6E6E6; padding: 1.5pt 0in 1.5pt 1.5pt;">
                <p><strong><u><span style="font-size: 9.0pt; font-family: 'Verdana','sans-serif';">Personal Details :</span></u></strong></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 5.25pt 0in 7.5pt 1.5pt;">
                <table style="width: 100.0%;" width="100%">
                <tbody>
                <tr>
                <td style="width: 22%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="22%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Father's Name </span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 76%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="76%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Jainal Abedin </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 22%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="22%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Mother's Name </span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 76%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="76%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Monowara Bagum </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 22%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="22%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Date of Birth</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 76%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="76%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">October 25, 1994 </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 22%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="22%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Gender</span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 76%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="76%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Male </span></p>
                </td>
                </tr>
                <tr>
                <td style="width: 22%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;" width="22%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Marital Status </span></p>
                </td>
                <td style="width: 2%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="2%">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="width: 76%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;" width="76%">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Unmarried </span></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Nationality</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Bangladeshi </span></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Religion</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Islam </span></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Permanent Address</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">H-119, Middle Bazaar, Powro 5 No, Daulatkhan, Bhola... 8310 </span></p>
                </td>
                </tr>
                <tr>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 3.75pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Current Location</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p style="text-align: center;"><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">:</span></p>
                </td>
                <td style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; padding: 1.5pt 0in 1.5pt 5.25pt;">
                <p><span style="font-size: 8.5pt; font-family: 'Verdana','sans-serif';">Dhaka </span></p>
                </td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                <p>&nbsp;</p>
              
            </div>        
              
              <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
    </html>
    
    """
    return HttpResponse(html_)
    #return HttpResponse("<h1>Its work..</h1>")
