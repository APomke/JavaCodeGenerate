service_template_str = """
package {{ package_name }}.service;

import com.baomidou.mybatisplus.extension.service.IService;
import {{ package_name_root }}.entity.{{ entity_name }};

import java.util.List;


public interface {{ class_name }} extends IService<{{ entity_name }}> {
    /**
    * @author admin
    * @version 1.0
    * @Description Service接口
    */
    // 查询
{% for entity in entity_list %}
    {% if entity.name == 'id' %}
    {{ entity_name }} get{{ entity_name }}By{{ entity.name_first }}({{ entity.type }} {{ entity.name }});
    {% else %}
    List<{{ entity_name }}> get{{ entity_name }}ListBy{{ entity.name_first }}({{ entity.type }} {{ entity.name }});
    {% endif %}

{%- endfor %}
    // 修改
    int update{{ entity_name }}({{ entity_name }} {{ entity_name | lower }});
    
    // 增加
    int add{{ entity_name }}({{ entity_name }} {{ entity_name | lower }});
    
    // 删除
    int delete{{ entity_name }}(String id);
    
}
"""