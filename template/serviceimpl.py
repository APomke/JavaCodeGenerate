serviceimpl_template_str = """
package {{ package_name }}.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import {{ package_name }}.mapper.{{ mapper_name }};
import {{ package_name }}.entity.{{ entity_name }};
import {{ package_name }}.service.{{ service_name }};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class {{ class_name }} extends ServiceImpl<{{ mapper_name }}, {{ entity_name }}> implements {{ service_name }} {

}
"""