const maxDepth = root => {
  let max = 0;                // tracks the deepest layer found so far
  if (!root) return max;      // base case: empty tree → 0

  const startingDepth = 1;    // root is level 1
  const stack = [[root, startingDepth]]; // initialize stack with tuple (node, depth)

  while (stack.length) {                // keep going until stack is empty
    let [node, depth] = stack.pop();    // pop the top tuple
    max = Math.max(max, depth);         // update max depth found so far

    // Push children onto the stack with incremented depth
    if (node.left) stack.push([node.left, depth + 1]);
    if (node.right) stack.push([node.right, depth + 1]);
  }

  return max;               // after visiting all nodes, max holds the tree’s depth
};
