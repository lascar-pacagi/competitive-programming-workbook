"""Publish Round IV from the course's already stress-tested algebra kernels.

Historical one-shot publisher.  The finale statements have since been edited
by hand (spoiler notes removed, statements completed); rerunning this script
overwrites those edits with the source statements.
"""
from pathlib import Path
import json, shutil

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'sections/100_grandmaster_finale/problems'
ITEMS=[
('31_connected_structure_series','Connected Structure Series','sections/90_master_polynomial_algebra_mixed/problems/b_connected_series'),
('32_rational_recurrence_samples','Rational Recurrence Samples','sections/90_master_polynomial_algebra_mixed/problems/a_rational_series'),
('33_subset_partition_spectrum','Subset Partition Spectrum','sections/89_polynomial_evaluation_subset_transforms/problems/d_subset_convolution'),
('34_xor_walk_spectrum','XOR Walk Spectrum','sections/89_polynomial_evaluation_subset_transforms/problems/c_xor_convolution'),
('35_polynomial_constraint_recovery','Polynomial Constraint Recovery','sections/90_master_polynomial_algebra_mixed/problems/d_recover_polynomial'),
('36_factorized_exponent_tower','Factorized Exponent Tower: Carmichael Kernel','sections/93_master_computational_number_theory_mixed/problems/b_carmichael_clock'),
('37_modular_root_catalogue','Modular Root Catalogue','sections/93_master_computational_number_theory_mixed/problems/d_power_congruence'),
('38_composite_discrete_log','Composite Discrete Log','sections/92_discrete_logs_modular_roots/problems/c_general_discrete_log'),
('39_summatory_multiplicative_blocks','Summatory Multiplicative Blocks','sections/35_math_mixed_contest/problems/m_totient_prefix'),
('40_gcd_convolution_queries','GCD Convolution Queries','sections/35_math_mixed_contest/problems/o_gcd_sum'),
]


def main():
 for slug,title,source in ITEMS:
  src=ROOT/source;dst=BASE/slug
  if dst.exists():shutil.rmtree(dst)
  shutil.copytree(src,dst)
  old=(dst/'README.md').read_text();body=old.split('\n',1)[1] if '\n' in old else ''
  (dst/'README.md').write_text(f'# {title}\n{body}')
  manifest=json.loads((dst/'manifest.json').read_text());manifest['title']=title
  (dst/'manifest.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
if __name__=='__main__':main()
