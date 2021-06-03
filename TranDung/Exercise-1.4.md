Exercise 1.4
The following exercise is intended to encourage you to think of testing in a more rigorous
way than you may be used to. The exercise also hints at the strong relationship between
specification clarity, faults, and test cases.
    
(a) Write a Java method with the signature
import java.util.Vector;

class Vector_test {
    public static Vector union (Vector a, Vector b) {
        Vector v = new Vector();
        v.addAll(a);
        v.addAll(b);
        return v;
    }
    public static void main(String[] args) {
        Vector a = new Vector();
        a.add(10);
        Vector b = new Vector();
        b.add(8);
        Vector v = union(a, b);
    }
}
    
(b) Upon reflection, you may discover a variety of defects and ambiguities in the given
assignment. In other words, ample opportunities for faults exist. Describe as many
possible faults as you can. (Note: Vector is a Java Collection class. If you are using
another language, interpret Vector as a list.)
One of possible fault is lack of verification statements such as checking the two vectors are empty or have different dimensions.
    
c) Create a set of test cases that you think would have a reasonable chance of revealing
the faults you identified above. Document a rationale for each test in your test set. If
possible, characterize all of your rationales in some concise summary. Run your tests
against your implementation.
Vector a = new Vector()
Vector b = new Vector()
    
Vector a = new Vector();
a.add(10)
Vector b = new Vector();
    
Vector a = new Vector();
Vector b = new Vector();
b.add(8)
    
(d) Rewrite the method signature to be precise enough to clarify the defects and ambiguities
identified earlier. You might wish to illustrate your specification with examples drawn
from your test cases.
public static Vector union(Vector a, Vector b, boolean inv = False)
{
  if (a.isEmpty() && b.isEmpty()) return Null;
  else
  {
    if (inv)
    {
      Vector v = new Vector();
      v.addAll(b);
      v.addAll(a);
      return v;
    }
    else
    {
      Vector v = new Vector();
      v.addAll(a);
      v.addAll(b);
      return v;
    }
  }
}