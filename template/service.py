service_template_str = """
package {{ package_name }}.service;

import com.baomidou.mybatisplus.extension.service.IService;
import {{ package_name_root }}.entity.{{ entity_name }};

public interface {{ class_name }} extends IService<{{ entity_name }}> {
    /**
    * @author admin
    * @version 1.0
    * @Description Service接口
    */

}
"""