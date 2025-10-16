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




const isBalanced = (root) => {
  // dfs() returns [isBalancedFlag, height]
  return dfs(root)[0] === 1;
};

const dfs = (root) => {
  // Base case: empty tree is balanced, height = 0
  if (!root) return [1, 0];

  // Recurse down to children
  const left = dfs(root.left);
  const right = dfs(root.right);

  const leftBalanced = left[0];
  const rightBalanced = right[0];
  const leftHeight = left[1];
  const rightHeight = right[1];

  // If either side is unbalanced, the whole subtree is unbalanced
  if (!leftBalanced || !rightBalanced) return [0, 0];

  // Check current node's balance condition
  if (Math.abs(leftHeight - rightHeight) > 1) return [0, 0];

  // If balanced → compute height for this node
  const height = 1 + Math.max(leftHeight, rightHeight);

  return [1, height];
};



// const isBalanced = (root) => {
//   // The helper dfs() returns [balancedFlag, height]
//   // balancedFlag: 1 if subtree is balanced, 0 otherwise
//   // height: height of the current subtree
//   return dfs(root)[0] === 1;
// };

// const dfs = (root) => {
//   // Base case — empty subtree is balanced and has height 0
//   if (!root) return [1, 0];

//   // Recurse to the leaves first
//   const left = dfs(root.left);
//   const right = dfs(root.right);

//   // Check three conditions to confirm balance:
//   // 1. Left subtree is balanced
//   // 2. Right subtree is balanced
//   // 3. Height difference ≤ 1
//   const balanced =
//     left[0] === 1 &&
//     right[0] === 1 &&
//     Math.abs(left[1] - right[1]) <= 1;

//   // Compute height of this node
//   const height = 1 + Math.max(left[1], right[1]);

//   // Return [balancedFlag, height]
//   return [balanced ? 1 : 0, height];
// };
