## How to make Presentations in Python

Have you been in a scenario where you made a bunch of plots in jupyter notebook, saved them, and copied them to powerpoint as part of a presentation, and then the data changes and you had to repeat the whole process again? I faced this issue multiple times when I started my Data Science career.

It was always frustrating to move charts from jupyter notebook to Powerpoint. Align the charts, format them and sometimes loose graphic quality on the plots. I hated it, and figured out a way to transition from jupyter notebook to high quality slides without loosing ability to refresh my slides when the data changes.

Heads up, this would require some understanding of matplotlib and a little OOP. Here's a list of steps we will follow:

- Create a figure class in a generic ppt dimension
- Sample page using the new figure class
- Generate plots using Penguin dataset
- Join all pages together.


Here's the final result.

Step 1: Create a figure class in a generic ppt dimension
Matplotlib has a figure class that can be customized. You can set background colors, add shapes, logos and more. Here's a sample.

Step 2: Sample page using the new figure class
A sample page is generated below using the figure class. You can treat the new figure class like you would treat the normal matplotlib figure.

Step 3: Generate plots using Penguin dataset
Here you can migrate sections of your code and data to generate the plot you need

Step 4: Join all pages together.
All pages are joined together to form a single pdf document. 

