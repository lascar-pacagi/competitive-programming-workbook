# Lazy Propagation Practice

1. Re-solve Section 37 C, `c_lazy_range_add_sum`, without looking at its code.
2. Extend that tree to range assignment plus range sum. Write the tag as
   `optional assigned value`, not as an additive delta.
3. Extend it again to binary range flip plus range-one-count. The tag is a
   boolean and composing it twice cancels it.

For each exercise, make a length-8 brute-force array and apply random updates
to both implementations. Check every range after every update. This catches
most tag-composition and push-order bugs before large tests do.
