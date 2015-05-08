Title: My Eleventh Post
Menulabel: My Post
Date: 2015-04-27 18:32
Category: programming
Tags: computer,geek,hadoop
Series: series1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ullamcorper urna id ante bibendum, ac accumsan mauris lacinia. Donec imperdiet fermentum purus vitae fermentum. Maecenas quis commodo urna. In eget tortor a metus vestibulum rhoncus. Nullam eu pellentesque velit, porta vehicula lacus. Vivamus rutrum convallis nulla vel rutrum. Phasellus malesuada interdum diam, vel tristique libero congue vitae. Sed a orci tellus. Morbi quis malesuada metus.

Donec est libero, lacinia vitae sapien eu, faucibus convallis nulla. Aenean accumsan volutpat pulvinar. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate fringilla velit ullamcorper sodales. In nec mi eu ante lobortis tristique ut et dolor. Aliquam molestie, mi vel aliquam ullamcorper, lectus nibh finibus eros, sed gravida sapien orci sed elit. Donec convallis dapibus arcu, nec ornare neque. In tellus metus, iaculis in efficitur quis, rutrum eu nisl.
```python
c = 3.00 * 10e8;
e = 1.60 * 10e-19;

lambdas = [1526717.557, 1652892.562, 1754385.965, 1980198.02, 2127659.574, 1136363.636, 1063829.787];
volts   = [1.337, 1.425, 1.529, 1.96, 2.08, 0.85, 0.764];

avg = 0;

for i in xrange(0,len(lambdas)):
  h = e/(lambdas[i]*(1/volts[i])*c);
  avg = avg + h;
  print "%s) h = %s" %(str(i+1), str(h));
print "Avg h = %s" % (str(avg/len(lambdas)));
```
Mauris imperdiet placerat lectus eu condimentum. Cras sodales velit eget lorem tempor ullamcorper. Cras quis diam sed leo faucibus condimentum. In velit metus, vulputate nec sapien a, cursus mollis augue. Duis nisl enim, accumsan sit amet ultrices sed, fringilla iaculis nisi. Nulla eleifend ex vel mauris interdum pharetra. Proin semper sagittis magna ullamcorper euismod. Curabitur bibendum orci viverra, finibus eros vel, vestibulum massa. Ut tristique iaculis odio, a pharetra nibh dapibus sit amet. Aliquam erat volutpat. Ut posuere scelerisque libero vitae porttitor. Vestibulum eget enim non magna efficitur lobortis in nec eros. Donec porta consectetur mattis. Sed ut faucibus felis. Nam quam enim, luctus euismod tristique non, accumsan a lectus. Quisque leo tellus, pharetra vel elit id, tempus facilisis metus.

Quisque pharetra, ante at porta aliquam, leo mauris malesuada augue, non varius felis lacus sit amet ligula. Donec sapien eros, gravida quis felis non, lobortis volutpat ipsum. Duis pellentesque aliquam tellus. Nunc porttitor, felis gravida gravida varius, quam libero rhoncus est, vitae porttitor tortor massa quis urna. Curabitur id rutrum ex. Vestibulum ac magna nec risus molestie pharetra. Vestibulum et faucibus lorem, eget vulputate nulla. Vivamus id felis nunc. Donec eleifend ex eget malesuada egestas. Donec a ante convallis, auctor nulla congue, dignissim lorem.

Quisque vestibulum faucibus eleifend. Cras eu augue id nisl lobortis porta ut sed nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque in dapibus lacus. Suspendisse eget est justo. Suspendisse sit amet metus at magna hendrerit scelerisque quis vitae leo. Proin consequat lectus sed ex tempus suscipit. Maecenas fermentum massa eu nulla finibus porta. Etiam sit amet mauris eu magna dapibus gravida et quis ligula.

