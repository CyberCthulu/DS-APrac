function isBalanced(root) {
  function check(node) {
    if (!node) return 0;  // base: empty tree has height 0

    const left = check(node.left);   // height of left
    const right = check(node.right); // height of right

    // If any subtree was already unbalanced, bubble up -1
    if (left === -1 || right === -1) return -1;

    // If height difference > 1 → not balanced
    if (Math.abs(left - right) > 1) return -1;

    // Otherwise, return current height
    return 1 + Math.max(left, right);
  }

  return check(root) !== -1;  // tree is balanced if we never saw -1
}
