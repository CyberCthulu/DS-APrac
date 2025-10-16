/**
 * Definition for a binary tree node (provided by LeetCode).
 * function TreeNode(val, left, right) {
 *   this.val = (val===undefined ? 0 : val);
 *   this.left = (left===undefined ? null : left);
 *   this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Returns true iff subRoot is a subtree of root.
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
const isSubtree = (root, subRoot) => {
  // Edge cases:
  // 1) Empty subRoot is always a subtree (matches "nothing" anywhere).
  if (!subRoot) return true;
  // 2) Non-empty subRoot can't be found in an empty root.
  if (!root) return false;

  // If trees match starting at this node, we are done.
  if (sameTree(root, subRoot)) return true;

  // Otherwise, search left and right subtrees of root.
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

/**
 * Returns true iff trees a and b are identical:
 *   - same structure AND same values everywhere.
 * This is a standard recursive "same tree" check.
 * @param {TreeNode} a
 * @param {TreeNode} b
 * @return {boolean}
 */
const sameTree = (a, b) => {
  // Both null -> identical at this branch.
  if (!a && !b) return true;

  // One null but not the other -> shapes differ.
  if (!a || !b) return false;

  // Values must match at this node...
  if (a.val !== b.val) return false;

  // ...and both left and right subtrees must match.
  return sameTree(a.left, b.left) && sameTree(a.right, b.right);
};


/**
 * O(N + M) approach using serialization + KMP substring search.
 * Use if interviewer asks to improve worst-case time.
 */
const isSubtreeKMP = (root, subRoot) => {
  const serialRoot = serialize(root);
  const serialSub  = serialize(subRoot);
  return kmpContains(serialRoot, serialSub);
};

/**
 * Preorder serialization with explicit null markers and separators.
 * This prevents false positives due to shape ambiguity.
 * Example node format: "^<val>" for nodes, "#," for nulls.
 */
const serialize = (node) => {
  const out = [];
  const dfs = (n) => {
    if (!n) { out.push("#,"); return; }      // null marker
    out.push("^", String(n.val), ",");       // node marker + value + sep
    dfs(n.left);
    dfs(n.right);
  };
  dfs(node);
  return out.join("");
};

/**
 * KMP substring search: does pattern occur in text?
 * Builds LPS (longest prefix-suffix) table to achieve linear time.
 */
const kmpContains = (text, pattern) => {
  if (pattern.length === 0) return true;
  const lps = buildLPS(pattern);

  let i = 0; // index in text
  let j = 0; // index in pattern
  while (i < text.length) {
    if (text[i] === pattern[j]) {
      i++; j++;
      if (j === pattern.length) return true; // full match
    } else {
      if (j > 0) j = lps[j - 1];
      else i++;
    }
  }
  return false;
};

const buildLPS = (p) => {
  const lps = Array(p.length).fill(0);
  let len = 0; // length of current longest prefix = suffix
  for (let i = 1; i < p.length; ) {
    if (p[i] === p[len]) {
      lps[i++] = ++len;
    } else {
      if (len > 0) len = lps[len - 1];
      else lps[i++] = 0;
    }
  }
  return lps;
};
