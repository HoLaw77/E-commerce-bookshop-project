<h1>Traverse Book</h1>

![logo](static/image/documentation/logo.png)


![responsiveness_mobile](static/documentations/responsiveness_mobile.png)
![responsiveness_desktop](static/documentations/responsiveness_desktop.png)

<p>Note: I have attempted to use amiresponsive but were unable to without a https url. so I used screenshot from chrome to show responsiveness</p>

<p>

[Traverse Book](https://ramensushibar707-cdc30d46d9dd.herokuapp.com/) is a full-stack project that enables user to make order and payment on books of different genres, languages, and cover.

</p>

<h2>How to Make Order</h2>

<li>User can choose to sign in or register first, then they can navigate to the book page and make their order by clicking into the book_detail page. It will lead them to the details of the books such as authors, ISBN, publisher, page numbers. They can make their order by clicking the add to cart button.</li> 

<li>User can also filter by searching the book they like by typing the name, author, or other keywords in the search bar.</li>

<li>After clicking the add to cart button, it will lead them to the order page which they can see the price of the book and the total price after adding the delivery cost which is 5% of the total price. There is also a button for them to proceed to checkout if they want. Otherwise, they can head back to the book page by clicking the button “Keep” shopping.</li>

<h3>Sign In page</h3>

![sign_in](static/documentations/sign_in.png)

<h3>Sign Up page</h3>

![sign_up](static/documentations/sign_up.png)

<h3>Navigation Bar at home page</h3>

![navigation_bar](static/image/documentation/topnav.png)


<h3>Search Bar at book page</h3>

![search_bar](static/image/documentation/search_bar.png)

<h3>Add to cart button</h3>

![add_to_cart_button](static/documentations/add_to_cart.png)

<br>
<br>
<h3>Order page, checkout button and keep shopping button</h3>
![order_page](static/documentations/order_page.png)

<br>

<h2>How to Check Order</h2>

<li>User can click on the "Check Your Order" button at the top right corner of the page to view and amend orders at the order.html page.</li>

<h3>Check Your Order button</h3>

![check_your_order](static/documentations/check_your_order.png)

<h2>How to check out and make payment</h2>
<li>User can check out by clicking the checkout button at the bottom of the order page.</li>
<li>It will lead the user to the checkout page where they can view their order displayed at the top of the page and a form for them to input their full name, email, phone number and address date. At the bottom of the page, there is a card payment field which enables them to type their card number, CVC code and the expiration date. </li>
<li>After submitting the payment form, there will be an authentication screen pops out by the Stripe 3D authentication to ensure that the payment is authenticated by the user. If the user declines the payment, it will lead them back to the checkout page with the form filled</li>

<li>If the payment is successful, it will lead the user to the checkout_success page where they will see the confirmation of the payment and the order number generated at the top of the page, with the order summary displayed again. They can also click continue shopping if they want to shop for more.</li>

<h3>Payment form</h3>

![payment_form](static/documentations/payment_form.png)

<h3>Checkout authentication by Stripe</h3>
![3d_authentication](static/documentations/3d_authentication.png)

<h3>Checkout Success Page </h3>
![checkout_success](static/documentations/checkout_success.png)

<h2>How to Delete and Edit Order</h2>
<li>User can delete order by clicking the remove button in each product in order page. After clicking it will remove the product and stay in the order page.</li>

<li> User can also adjust the number of books they want by clicking the number bar to adjust, by clicking the submit button, it will update the number of books and price automatically.</li>

<h3>Adjust button and Remove button for each product in order page</h3>

![edit_and_delete_order](static/documentations/edit_and_delete_order.png)

<h2>Development</h2>
<h3> Original Flowchart and Wireframe</h3>

![wire_frame_1](static/documentations/wire_frame_1.png)
![wire_frame_2](static/documentations/wire_frame_2.png)
![wire_frame_3](static/documentations/wire_frame_3.png)

![flow_chart](static/documentations/Flowchart%20Template.png)

<li>In my original setting, I would like to offer user choices in filtering the books according to genre, covers, and, languages.</li>
<li>After doing more research and building the page, I realise that it would be too complicated so I simplified by only keeping the search bar.</li>
<li>I have also added a login and sign off function using django allauth functionality.</li>

<h2>Market Research</h2>

<li> The initial idea of this online bookshop comes from my personal experience as a multilingual reader living in UK. It is observable that not enough source of selling books of different languages available in English speaking countries. The title of the page “Traverse Book” wishes to represent the idea to traverse the language and cultural border and encompass more books from different languages, genre, and covers.</li>

<li>To achieve that, I have tried to input books of different languages apart from English such as Chinese, France, Japanese in order to make this available. There will be room for further development if there is more stock in my knowledge.</li>

<h3>Agile approach in development </h3>

![agile_example](static/documentations/agile_example.png)

<li>I have follow the agile approach in this project by setting up various issues to improve my project throughout the development process</li>
<li>[add filter link??????] </li>


<h2>Testing</h2>
<li>I tested that this page works in different browser such as: Chrome, Microsoft-edge, Firefox.</li>
<li>I confirmed the project is responsive, look goods and function on all standard size screen using devtool device tool bar.</li>
<li>Code tested in my local terminal and confirmed using coverage.</li>

![Python_Automated_Test_coverage_Report](static/documentations/python_coverage_test_report.png)
<p>Coverage report for python automated test</p>

<h2>Bugs</h2>

<h3>Solving bugs</h3>

<li>When I tried to build the stripe authentication. I realise that it is not working and the payment is not submitted successfully. Upon checking, I realise the id I have in the stripe_element.js does not match the one I have in the checkout.html. After uniting it, I can see the screen popped out with a valid card inputted.</li>

<li>When I am building the order.html, I cannot render the order to the template. After checking with mentor, I realise the problem is in the context because I previously added the order model in the Order app which confused the Django with the context tag “order” which I used to render the order in order.html. Therefore, I changed the context tag to item and moved the order model to checkout app, it has become available since then.</li>

<h2>Validation Testing</h2>
<li>HTML: No error was found using official W3C Validator.</li>
<li>CSS: No error was found using official W3C Validator.</li>
<li>Accesssibility: I confirm the design and layout of the page is easy to read and accessible by running it through lighthouse in devtools.
</li>
<li>PEP8: No Errors return from https://pep8ci.herokuapp.com/# </li>

![lighthouse](static/documentations/lighthouse_testing.png)
<h2>Deployment</h2>

<p>The page is deployed using heroku, following the below steps:</p>

<li> Install the heroku CLI in IDE terminal</li>
<li>Install Project requirements app </li>
<li>Create the heroku app</li>
<li>Create a database in ElephantSQL</li>
<li>Connecting our Remote Database</li>
<li>Pushing changes to Github</li>
<li>Fix ALLOWED_HOSTS and Run the Project</li>
<li>Connecting Heroku to Github</li>
<li>Set The SECRET_KEY in setting.py</li>
<li>Once the link is deployed, the link is generated</li>

<p>The link is below https://ramensushibar707-cdc30d46d9dd.herokuapp.com/</p>


<h2>Credit</h2>

<h3>Code</h3>

<li>Model structure has been advised by my mentor Juliia Konovalov. Many Thanks for his patient and helpful guidance.</li>

<li>checkout app and templates, filter and searching, payment structure are inspired by tutorial of Boutique Ado project in Code Institute course.

[Boutique_Ado_Github](https://docs.google.com/document/d/1P5Mzkvzm3HUMrMgABn1KwU_pHnR5n4TUX8rHKB-9CMA/edit)
</li>

<li>Edit and delete order button is inspired by the handout of Hello Django project in Code Institute course

[Hello Django: Part 7: Modifying Data](https://docs.google.com/document/d/1RNDHMuQEBJ8if9XYR1WLjNJx_Z4Nad-NarjRVFrC0gQ/edit#heading=h.hvy9tw74f1o0)
</li>

<li>testing format has been inspired by handout of Hello Django project in Code Institute modules

[Hello Django: Part 8: Testing](https://docs.google.com/document/d/1L7zyIXL1wCki2eOoDZPCw9fIIe93NfdCiA_mbht9P8A/edit#heading=h.hvy9tw74f1o0)

</li>


<h3>Media</h3>

<h4>Index.html</h4>
<p>https://www.pinterest.com/pin/292593307016180845/</p>


<h4>book.html</h4>
<p>https://www.flickr.com/photos/o_0/41785994071</p>
<p>https://www.flickr.com/photos/95268887@N00/2392523070</p>
<p>https://www.flickr.com/photos/huixuan/1350811859/</p>
<p>https://www.pinterest.com/pin/266275396692800295/</p>
<p>https://pleasurepalate.blogspot.com/2009/02/im-in-mood-for-soup.html</p>
<p>https://www.flickr.com/photos/62942199@N08/48023829601/</p>
<p>https://www.flickr.com/photos/mmm-yoso/44764296142/</p>
<p>https://www.flickr.com/photos/62942199@N08/33497523872</p>
<p>https://www.recetasjaponesas.com/2015/05/gyoza.html</p>
<p>https://www.kampustani.com/teknologi-penanganan-pasca-panen-kedelai/</p>
<p>https://www.dream.co.id/culinary/resep-yakitori-sate-kulit-ayam-manis-ala-jepang-200625r.html</p>
<p>https://dude4food.blogspot.com/2016/11/a-tenya-christmas-with-tenya-tempura.html</p>
<p>https://www.angsarap.net/2014/10/28/kimchi/</p>
<p>https://michaeltoa.com/japanese-fried-chicken-chicken-karaage-5c52c05e4805?gi=3f92a80ddfa5</p>


